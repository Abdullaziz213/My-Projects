package the_american_dream_autoverleih_abdullaziz;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class JsonUtil {
    private static final String FILE_PATH = "users.json";

    public static List<User> readUsers() throws IOException {
        List<User> users = new ArrayList<>();
        if (Files.exists(Paths.get(FILE_PATH))) {
            String content = new String(Files.readAllBytes(Paths.get(FILE_PATH)));
            if (!content.isEmpty()) {
                content = content.trim();
                if (content.startsWith("[")) {
                    content = content.substring(1, content.length() - 1);
                    String[] userEntries = content.split("(?<=}),");
                    for (String entry : userEntries) {
                        entry = entry.trim();
                        if (entry.endsWith(",")) {
                            entry = entry.substring(0, entry.length() - 1);
                        }
                        users.add(parseUser(entry));
                    }
                }
            }
        }
        return users;
    }

    private static User parseUser(String json) {
        json = json.replace("{", "").replace("}", "").replace("\"", "");
        String[] parts = json.split(", ");
        String name = parts[0].split(":")[1];
        String email = parts[1].split(":")[1];
        String password = parts[2].split(":")[1];
        return new User(name, email, password);
    }

    public static void writeUsers(List<User> users) throws IOException {
        StringBuilder json = new StringBuilder();
        json.append("[");
        for (int i = 0; i < users.size(); i++) {
            json.append(users.get(i).toString());
            if (i < users.size() - 1) {
                json.append(",");
            }
        }
        json.append("]");
        Files.write(Paths.get(FILE_PATH), json.toString().getBytes());
    }
}