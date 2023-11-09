package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.google.android.material.navigation.NavigationView;

public class MainActivity extends AppCompatActivity {

    private DrawerLayout drawerLayout;
    private AppBarConfiguration appBarConfiguration;
    private NavController navController;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button startCatalogButton = findViewById(R.id.startCatalogButton);
        startCatalogButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Iniciar CatalogActivity
                Intent intent = new Intent(MainActivity.this, CatalogActivity.class);
                startActivity(intent);
            }
        });

        drawerLayout = findViewById(R.id.drawer_layout);

        // Configura el NavController
        navController = Navigation.findNavController(this, R.id.nav_host_fragment);

        // Configura el AppBarConfiguration
        appBarConfiguration = new AppBarConfiguration.Builder(
                R.id.catalogFragment,
                R.id.aboutFragment
        ).setOpenableLayout(drawerLayout).build();

        // Configura la navegación con el AppBarConfiguration y NavController
        NavigationUI.setupWithNavController(findViewById(R.id.toolbar), navController, appBarConfiguration);
        NavigationUI.setupWithNavController((NavigationView) findViewById(R.id.navigation_view), navController);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        getSupportActionBar().setHomeButtonEnabled(true);
    }

    @Override
    public boolean onSupportNavigateUp() {
        return NavigationUI.navigateUp(navController, appBarConfiguration) || super.onSupportNavigateUp();
    }
}
