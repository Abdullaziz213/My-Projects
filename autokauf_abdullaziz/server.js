const bodyParser = require('body-parser');
const fs = require('fs');
const mongoose = require('mongoose');


mongoose.connect('mongodb+srv://abdullazizhassenabdella:1234@cluster.mijlazq.mongodb.net/mongodbtest1?retryWrites=true&w=majority&appName=Cluster').then(() => console.log('DB Connection successful!'))


const Auto = mongoose.model('Auto', new mongoose.Schema({
  marke: String,
  preis: Number,
  baujahr: Number,
  name: String 
}));

if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config();
}

const express = require('express');
const app = express();
const bcrypt = require('bcrypt');
const passport = require('passport');
const flash = require('express-flash');
const session = require('express-session');
const methodOverride = require('method-override');

const initializePassport = require('./passport-config');
initializePassport(
  passport,
  (email) => users.find((user) => user.email === email),
  (id) => users.find((user) => user.id === id)
);

const users = [];

app.set('view-engine', 'ejs');
app.use(express.urlencoded({ extended: false }));
app.use(flash());
app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
  })
);
app.use(passport.initialize());
app.use(passport.session());
app.use(methodOverride('_method'));
app.use(bodyParser.json());

app.get('/', checkAuthenticated, (req, res) => {
  res.render('index.ejs', { name: req.user.name });
});

app.get('/login', checkNotAuthenticated, (req, res) => {
  res.render('login.ejs');
});

app.post(
  '/login',
  checkNotAuthenticated,
  passport.authenticate('local', {
    successRedirect: '/',
    failureRedirect: '/login',
    failureFlash: true,
  })
);

app.get('/register', checkNotAuthenticated, (req, res) => {
  res.render('register.ejs');
});

app.get('/kauf', (req, res) => {
  res.render('kauf.ejs');
});


app.get('/verkauf', (req, res) => {
  res.render('verkauf.ejs');
});


app.get('/inserieren', (req, res) => {
  res.render('inserieren.ejs');
});

app.get('/autos', checkAuthenticated, async (req, res) => {
  try {
    const autos = await Auto.find();
    res.json(autos);
  } catch (error) {
    console.error('Fehler beim Abrufen der Autos:', error);
    res.status(500).json({ error: 'Interner Serverfehler' });
  }
});

app.get('/meine-autos', checkAuthenticated, async (req, res) => {
  try {
    const userName = req.user.name;
    const userAutos = await Auto.find({ name: userName });
    res.json(userAutos);
  } catch (error) {
    console.error('Fehler beim Abrufen der Autos:', error);
    res.status(500).json({ error: 'Interner Serverfehler' });
  }
});


app.post('/register', checkNotAuthenticated, async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    users.push({
      id: Date.now().toString(),
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword,
    });
    res.redirect('/login');
  } catch {
    res.redirect('/register');
  }
});

app.post('/inserieren', checkAuthenticated, async (req, res) => {
  const { marke, preis, baujahr } = req.body;

  if (!marke || !preis || !baujahr) {
    return res.status(400).json({ error: 'Bitte geben Sie Marke, Preis und Baujahr an.' });
  }

  try {
    const auto = new Auto({
      marke,
      preis,
      baujahr,
      name: req.user.name
    });
    await auto.save();
    res.redirect('/verkauf');
  } catch (error) {
    console.error('Fehler beim Speichern des Autos:', error);
    res.status(500).json({ error: 'Interner Serverfehler' });
  }
});



app.delete('/logout', (req, res) => {
  req.logout(function (err) {
    if (err) {
      return next(err);
    }
    res.redirect('/login');
  });
});

function checkAuthenticated(req, res, next) {
  if (req.isAuthenticated()) {
    return next();
  }

  res.redirect('/login');
}

function checkNotAuthenticated(req, res, next) {
  if (req.isAuthenticated()) {
    return res.redirect('/');
  }
  next();
}


const AutoOperations = {
  getAutosByUsername: function (autos, username) {
    return autos.filter(auto => auto.name === username);
  }
};

module.exports = AutoOperations;



app.listen(8000);
