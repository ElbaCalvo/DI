package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    private Button firstButton; // Declaración de un objeto Button llamado firstButton
    Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState); // Llama al método onCreate.
        setContentView(R.layout.activity_catalog); // Establece el diseño de la actividad desde el XML.
        firstButton = findViewById(R.id.button); // Busca el botón por su ID.

        firstButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) { // Cuando se presione el click.
                Intent intent = new Intent(context, DetailActivity.class); // Intent para abrir la actividad DetailActivity
                startActivity(intent); // Inicia la actividad DetailActivity.
            }
        });
    }
}