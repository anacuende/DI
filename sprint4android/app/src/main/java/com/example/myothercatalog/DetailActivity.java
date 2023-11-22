package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.squareup.picasso.Picasso;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        Intent intent = getIntent();
        // Obtener los datos
        String name = intent.getStringExtra("name");
        String description = intent.getStringExtra("description");
        String imageUrl = intent.getStringExtra("imageUrl");

        // Referenciar los elementos
        TextView textViewName = findViewById(R.id.textViewTitle);
        TextView textViewDescription = findViewById(R.id.textViewDescription);
        ImageView imageViewGame = findViewById(R.id.imageView);

        // Establecer los datos en los elementos
        textViewName.setText(name);
        textViewDescription.setText(description);
        Picasso.get().load(imageUrl).into(imageViewGame);
    }
}