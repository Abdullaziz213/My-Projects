package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class hauptnach {
    @FXML
    private Button zurueck;

    @FXML
    private Button camero_2011;

    @FXML
    private Button challanger_2008;

    @FXML
    private Button charger_1967;

    @FXML
    private Button mustang_2018;

    @FXML
    private Button hilfebutton;


    @FXML
    void camero2011(ActionEvent event) throws IOException {
        App.setRoot("camero2011");
    }

    @FXML
    void challanger2008(ActionEvent event) throws IOException {
        App.setRoot("challanger2008");
    }

    @FXML
    void charger2020(ActionEvent event) throws IOException {
        App.setRoot("charger2020");
    }

    @FXML
    void hilfe(ActionEvent event) throws IOException {
        App.setRoot("Hilfe");
    }

    @FXML
    void mustang2018(ActionEvent event) throws IOException {
        App.setRoot("mustang2018");
    }

    @FXML
    void zurueck(ActionEvent event) throws IOException {
        App.setRoot("haupt");
    }
}
