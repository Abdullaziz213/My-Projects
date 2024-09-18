package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class autonach {
    @FXML
    private Button zurueck;

    @FXML
    private Button mieten;

    @FXML
    void mieten(ActionEvent event) throws IOException {
        App.setRoot("Mieten");
    }

    @FXML
    void zurueck(ActionEvent event) throws IOException {
        App.setRoot("hauptnach2006");
    }
}
