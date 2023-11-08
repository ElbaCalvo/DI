package com.example.mycatalog;

import androidx.activity.OnBackPressedCallback;
import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;

import com.google.android.material.navigation.NavigationView;

import android.content.Context;
import android.os.Bundle;
import android.view.MenuItem;

import androidx.appcompat.widget.Toolbar;
import androidx.fragment.app.Fragment;

public class MainActivity extends AppCompatActivity {
    private Context context = this;
    private Toolbar toolbar;
    private DrawerLayout drawerLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState); // Llama al método onCreate.
        setContentView(R.layout.activity_main); // Establece el diseño de la actividad desde el XML.

        drawerLayout = findViewById(R.id.drawerLayout); // Referencia al DrawerLayout desde el archivo XML.
        toolbar = findViewById(R.id.toolbar); // Referencia a la barra de herramientas desde el archivo XML.

        // Configura botón Atrás que cierra el menú deslizante si está abierto.
        getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
            @Override
            public void handleOnBackPressed() {
                if(drawerLayout.isDrawerOpen(GravityCompat.START)){
                    drawerLayout.closeDrawer(GravityCompat.START);
                }
            }
        });

        setSupportActionBar(toolbar); // Configura la barra de herramientas.
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);

        drawerLayout.addDrawerListener(toggle); // Gestiona el deslizamiento del menú.
        toggle.syncState(); // Sincroniza el estado del ActionBarDrawerToggle.

        NavigationView navigationView = findViewById(R.id.navigationView); // Obtiene una referencia a la vista de navegación desde el archivo XML.
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                Fragment fragment = null;

                // Verifica qué elemento del menú se seleccionó y crea un fragmento correspondiente.
                if(item.getItemId()==R.id.item1){
                    fragment = new Fragment1();
                }

                if(item.getItemId()==R.id.item2){
                    fragment = new Fragment2();
                }

                // Si se selecciona un fragmento válido, reemplaza el contenido de los fragmentos.
                if (fragment != null){
                    getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, fragment).commit();
                    drawerLayout.closeDrawer(GravityCompat.START); // Cierra el menú deslizante.
                    return true;
                }
                return false;
            }
        });
    }
}
