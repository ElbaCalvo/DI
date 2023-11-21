package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class FruitsData {
    private String name;
    private String imageUrl;
    private String description;

    // Constructor.
    public FruitsData(String name, String imageUrl){
        this.name = name;
        this.imageUrl = imageUrl;
    }

    public String getName() {
        return name;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public String getDescription() { return description; }

    // Constructor para inicializar los datos desde un objeto JSONObject.
    public FruitsData(JSONObject json){
        try{
            this.name=json.getString("name");
            this.imageUrl=json.getString("image_url");
            this.description=json.getString("description");
        }catch(JSONException e){
            e.printStackTrace();
        }
    }
}
