package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;
import java.util.List;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class SecondaryController {

    @FXML
    private TextField t_email_r;

    @FXML
    private TextField t_passwort_r;

    @FXML
    private Button rege_button;

    @FXML
    private TextField t_name;

    @FXML
    private Button zurueck_reg;

    @FXML
    void regestrieren(ActionEvent event) {
        String name = t_name.getText();
        String email = t_email_r.getText();
        String passwort = t_passwort_r.getText();

        try {
            if (registerUser(name, email, passwort)) {
                // Zeige eine Erfolgsmeldung an
                showAlert("Registrierung erfolgreich", "Der Benutzer wurde erfolgreich registriert.");
                App.setRoot("login");
            } else {
                showAlert("Registrierung fehlgeschlagen", "Ein Benutzer mit dieser E-Mail existiert bereits.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    void zurueck(ActionEvent event) throws IOException {
        App.setRoot("login");
    }

    private boolean registerUser(String name, String email, String passwort) throws IOException {
        List<User> users = JsonUtil.readUsers();

        // Überprüfen, ob die E-Mail bereits existiert
        boolean emailExists = users.stream().anyMatch(user -> user.getEmail().equals(email));
        if (emailExists) {
            return false;
        }

        // Neuen Benutzer hinzufügen
        User newUser = new User(name, email, passwort);
        users.add(newUser);
        JsonUtil.writeUsers(users);
        return true;
    }

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}