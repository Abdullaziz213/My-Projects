package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class hilfe {
    @FXML
    private Button zurueck_knopf;

    @FXML
    private Button naechstes_knopf;


    @FXML
    void naechstes_1(ActionEvent event) throws IOException {
        App.setRoot("Hilfe2");
    }

    @FXML
    void naechstes_2(ActionEvent event) throws IOException {
        App.setRoot("Hilfe3");
    }

    @FXML
    void naechstes_3(ActionEvent event) throws IOException {
        App.setRoot("Hilfe4");
    }

    @FXML
    void naechstes_4(ActionEvent event) throws IOException {
        App.setRoot("Hilfe");
    }

    @FXML
    void zurueck(ActionEvent event) throws IOException {
        App.setRoot("haupt");
    }
}
