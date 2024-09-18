const AutoOperations = require('../server');

describe("Autotests", () => {
    test("Hole Autos nach Benutzername", () => {
      
      const existingAutos = [
        { marke: 'Audi', preis: 20000, baujahr: 2018, name: 'TestUser1' },
        { marke: 'BMW', preis: 25000, baujahr: 2019, name: 'TestUser2' },
        { marke: 'Mercedes', preis: 30000, baujahr: 2020, name: 'TestUser1' }
      ];
      const username = 'TestUser1';
  
      
      const userAutos = AutoOperations.getAutosByUsername(existingAutos, username);
  
      
      expect(userAutos).toHaveLength(2);
      expect(userAutos.every(auto => auto.name === username)).toBe(true);
    });
});