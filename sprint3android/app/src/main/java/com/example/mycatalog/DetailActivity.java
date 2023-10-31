package com.example.mycatalog;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    private ImageView imagen;
    private TextView descripcion;
    private Button meGustaButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState); // Llama al método onCreate.
        setContentView(R.layout.activity_detail); // Establece el diseño de la actividad desde el XML.
    }
}
