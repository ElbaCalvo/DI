package com.example.myothercatalog;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {
    private TextView nameTextView;
    private ImageView fruitImageView;
    private TextView descriptionTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

        Intent intent = getIntent();
        if (intent != null) {
            String fruitName = intent.getStringExtra("fruit_title");
            String fruitImageUrl = intent.getStringExtra("fruit_image");
            String fruitDescription = intent.getStringExtra("fruit_description");

            // Encontrar las vistas en el layout de la DetailActivity.
            TextView nameTextView = findViewById(R.id.text_view1);
            ImageView fruitImageView = findViewById(R.id.image_view);
            TextView descriptionTextView = findViewById(R.id.text_view2);

            // Establecer los datos en las vistas.
            nameTextView.setText(fruitName);
            descriptionTextView.setText(fruitDescription);

            Glide.with(this) // Utilizar Glide para cargar la imagen desde la URL.
                    .load(fruitImageUrl) // Cargar la imagen.
                    .circleCrop() // Transforma la imagen en circular.
                    .into(fruitImageView); // Colocar la imagen.
        }
    }
}
