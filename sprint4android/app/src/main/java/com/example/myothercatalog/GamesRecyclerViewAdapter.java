package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.squareup.picasso.Picasso;
import java.util.List;

public class GamesRecyclerViewAdapter extends RecyclerView.Adapter<GamesRecyclerViewAdapter.ViewHolder> {
    private List<GamesData> gamesDataList;
    private Activity activity;
    private OnItemClickListener onItemClickListener;
    // Interfaz que gestiona los clicks
    public interface OnItemClickListener {
        void onItemClick(GamesData gamesData);
    }
    // Establecer el Listener
    public void setOnItemClickListener(OnItemClickListener listener) {
        this.onItemClickListener = listener;
    }
    // Constructor que recibe la lista de datos y la actividad
    public GamesRecyclerViewAdapter(List<GamesData> gamesDataList, Activity activity) {
        this.gamesDataList = gamesDataList;
        this.activity = activity;
    }
    // Método llamado cuando se crea un nuevo ViewHolder
    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Infla el XML de la celda y devuelve un nuevo ViewHolder
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_game, parent, false);
        return new ViewHolder(view);
    }
    // Método que establece los datos en un ViewHolder concreto
    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        // Obtiene los datos del juego en la posición especificada
        GamesData gamesData = gamesDataList.get(position);
        // Establece el título en el TextView
        holder.textViewTitle.setText(gamesData.getName());
        // Carga la imagen utilizando Picasso y la URL
        Picasso.get().load(gamesData.getImageUrl()).into(holder.imageViewGame);
        // Establece un click en un elemento de la lista
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (onItemClickListener != null) {
                    onItemClickListener.onItemClick(gamesData);
                }
            }
        });
    }
    // Devuelve la cantidad de elementos en la lista
    @Override
    public int getItemCount() {
        return gamesDataList.size();
    }
    // Representa el ViewHolder de la celda
    public static class ViewHolder extends RecyclerView.ViewHolder {
        TextView textViewTitle;
        ImageView imageViewGame;
        // Constructor que asigna las vistas del XML a las variables de la clase ViewHolder
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            textViewTitle = itemView.findViewById(R.id.text_view_title);
            imageViewGame = itemView.findViewById(R.id.image_view_game);
        }
    }
}
