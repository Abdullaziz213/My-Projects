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

public class PrimaryController {

    @FXML
    private TextField t_email;

    @FXML
    private TextField t_passwort;

    @FXML
    private Button anmelden;

    @FXML
    private Button rege;

    @FXML
    void anmelden(ActionEvent event) {
        String email = t_email.getText();
        String passwort = t_passwort.getText();

        try {
            if (authenticate(email, passwort)) {
                // Lade das Hauptfenster
                App.setRoot("haupt");
            } else {
                showAlert("Login fehlgeschlagen", "E-Mail oder Passwort ist falsch.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    void regewechsel(ActionEvent event) throws IOException {
        App.setRoot("secondary");
    }

    private boolean authenticate(String email, String passwort) throws IOException {
        List<User> users = JsonUtil.readUsers();
        return users.stream().anyMatch(user -> user.getEmail().equals(email) && user.getPassword().equals(passwort));
    }

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }


    @FXML
    private Button weiter;

    @FXML
    void weiter(ActionEvent event) throws IOException {
        App.setRoot("haupt");
    }
}



