package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.util.List;

public class FruitsViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;

    public FruitsViewHolder(@NonNull View itemView, List<FruitsData> allTheData) {
        super(itemView);
        // Inicialización de los elementos.
        textView = (TextView) itemView.findViewById(R.id.fruits_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.fruits_image_view);

        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Acciones al hacer clic en el botón.
                CallDetailActivity(getAdapterPosition(), itemView.getContext(), allTheData);
            }
        });
    }

    public void CallDetailActivity(int position, Context context, List<FruitsData> allTheData){
        Intent intent = new Intent(context, DetailActivity.class);
        FruitsData selectedFruit = allTheData.get(position);
        intent.putExtra("fruit_title", selectedFruit.getName());
        intent.putExtra("fruit_image", selectedFruit.getImageUrl());
        intent.putExtra("fruit_description", selectedFruit.getDescription());
        itemView.getContext().startActivity(intent);
    }

    public void showData(FruitsData data, Activity activity){
        // Mostrar los datos.
        textView.setText(data.getName());
        Glide.with(itemView.getContext()) // Utilizar Glide para cargar la imagen desde la URL.
            .load(data.getImageUrl()) // Cargar la imagen.
            .into(imageView); // Colocar la imagen.
    }
}
