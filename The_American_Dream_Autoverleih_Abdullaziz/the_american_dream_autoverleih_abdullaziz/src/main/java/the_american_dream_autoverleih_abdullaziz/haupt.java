package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class haupt {
    @FXML
    private Button abmelden_button;

    @FXML
    private Button vorbutton;

    @FXML
    private Button nachbutton;

    @FXML
    private Button hilfebutton;

    @FXML
    void abmelden(ActionEvent event) throws IOException {
        App.setRoot("login");
    }

    @FXML
    void hilfe(ActionEvent event) throws IOException {
        App.setRoot("hilfe");
    }

    @FXML
    void nach2005(ActionEvent event) throws IOException {
        App.setRoot("hauptnach2006");
    }

    @FXML
    void vor2005(ActionEvent event) throws IOException {
        App.setRoot("hauptvor2005");
    }
}
