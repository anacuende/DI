package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        TextView textViewDetail = findViewById(R.id.textViewDetail);
        String detailText = "Este es el detalle de tu elemento.";
        textViewDetail.setText(detailText);
    }
}