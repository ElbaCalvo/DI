package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class FruitsViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;
    public FruitsViewHolder(@NonNull View itemView) {
        super(itemView);
        // Inicialización de los elementos.
        textView = (TextView) itemView.findViewById(R.id.fruits_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.fruits_image_view);
    }

    public void showData(FruitsData data, Activity activity){
        // Mostrar los datos.
        textView.setText(data.getName());
        Glide.with(itemView.getContext()) // Utilizar Glide para cargar la imagen desde la URL.
            .load(data.getImageUrl()) // Cargar la imagen.
            .into(imageView); // Colocar la imagen.
    }
}
