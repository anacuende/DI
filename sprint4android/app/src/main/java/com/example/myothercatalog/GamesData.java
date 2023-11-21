package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class GamesData {
    private String name;
    private String description;
    private String imageUrl;
    // Constructor que recibe un objeto JSON y extrae los datos
    public GamesData(JSONObject jsonObject) {
        try {
            this.name = jsonObject.getString("name");
            this.description = jsonObject.getString("description");
            this.imageUrl = jsonObject.getString("image_url");
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    // Obtener los datos del juego
    public String getName() {
        return name;
    }
    public String getDescription() {
        return description;
    }
    public String getImageUrl() {
        return imageUrl;
    }
}
