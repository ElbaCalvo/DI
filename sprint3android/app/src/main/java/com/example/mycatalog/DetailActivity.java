package com.example.mycatalog;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState); // Llama al método onCreate.
        setContentView(R.layout.activity_detail); // Establece el diseño de la actividad desde el XML.
    }
}
