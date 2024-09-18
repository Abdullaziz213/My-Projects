package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class hauptvor {
    @FXML
    private Button zurueck_vor;

    @FXML
    private Button camero_1968;

    @FXML
    private Button challanger_1971;

    @FXML
    private Button charger_1967;

    @FXML
    private Button mustang_1967;

    @FXML
    private Button hilfebutton;

    @FXML
    void camero1968(ActionEvent event) throws IOException {
        App.setRoot("cheverolet1967");
    }

    @FXML
    void challanger1971(ActionEvent event) throws IOException {
        App.setRoot("challanger1971");
    }

    @FXML
    void charger1967(ActionEvent event) throws IOException {
        App.setRoot("charger1970");
    }

    @FXML
    void hilfe(ActionEvent event) throws IOException {
        App.setRoot("Hilfe");
    }

    @FXML
    void mustang1967(ActionEvent event) throws IOException {
        App.setRoot("mustang1967");
    }

    @FXML
    void zurueckvor(ActionEvent event) throws IOException {
        App.setRoot("haupt");
    }
}
