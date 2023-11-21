package com.example.myothercatalog;

import android.app.Activity;
import android.os.Bundle;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Obtener el ID del RecyclerView en el XML
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        // Obtener la referencia a la actividad actual
        Activity activity = this;
        // Crear solicitud para obtener el JSON de la URL
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/anacuende/DI/main/recursos/Ejercicio2.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Crear una lista para guardar los datos del JSON
                        List<GamesData> allTheGames = new ArrayList<>();
                        // Itera a través de la respuesta JSON para obtener los datos
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                // Obtiene el objeto JSON que representa un juego
                                JSONObject game = response.getJSONObject(i);
                                // Crea un objeto GamesData a partir del juego y lo añade a la lista
                                GamesData data = new GamesData(game);
                                allTheGames.add(data);
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }
                        // Crear un adaptador con la lista de datos
                        GamesRecyclerViewAdapter adapter = new GamesRecyclerViewAdapter(allTheGames, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Muestra un mensaje de error
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
        // Crea una cola de solicitudes y añade la solicitud a la cola
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }
}
