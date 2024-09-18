package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

public class mieten {

    public int carcost;

    public int dayscost;

    public int cost;



    @FXML
    private Button camero1968;

    @FXML
    private Button zurueck;

    @FXML
    private Button tag1;

    @FXML
    private Button camero2011;

    @FXML
    private Button challanger1971;

    @FXML
    private Button challanger2008;

    @FXML
    private Button mustang1967;

    @FXML
    private Button mustang2018;

    @FXML
    private Button charger1970;

    @FXML
    private Button charger2020;

    @FXML
    private Button tag2;

    @FXML
    private Button tag3;

    @FXML
    private Button tag4;

    @FXML
    private Button tag5;

    @FXML
    private Button rechnen;

    @FXML
    private Button mieten;

    @FXML
    private Label label_label;

    @FXML
    void camero1968(ActionEvent event) {
        carcost = 450;
    }

    @FXML
    void camero2011(ActionEvent event) {
        carcost = 300;
    }

    @FXML
    void challanger1971(ActionEvent event) {
        carcost = 375;
    }

    @FXML
    void challanger2008(ActionEvent event) {
        carcost = 350;
    }

    @FXML
    void charger1970(ActionEvent event) {
        carcost = 400;
    }

    @FXML
    void charger2020(ActionEvent event) {
        carcost = 500;
    }

    @FXML
    void mieten(ActionEvent event) throws IOException {
        App.setRoot("danke");
    }

    @FXML
    void mustang1967(ActionEvent event) {
        carcost = 390;
    }

    @FXML
    void mustang2018(ActionEvent event) {
        carcost = 400;
    }

    @FXML
    void rechnen(ActionEvent event) {
        cost = carcost + dayscost;
        label_label.textProperty().bind(new SimpleIntegerProperty(cost).asString());
    }

    @FXML
    void tag1(ActionEvent event) {
        dayscost = 0;
    }

    @FXML
    void tag2(ActionEvent event) {
        dayscost = 200;
    }

    @FXML
    void tag3(ActionEvent event) {
        dayscost = 400;
    }

    @FXML
    void tag4(ActionEvent event) {
        dayscost = 600;
    }

    @FXML
    void tag5(ActionEvent event) {
        dayscost = 800;
    }

    @FXML
    void zurueck(ActionEvent event) throws IOException {
        App.setRoot("haupt");
    }

}
