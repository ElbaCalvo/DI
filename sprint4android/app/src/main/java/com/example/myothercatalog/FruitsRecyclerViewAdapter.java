package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class FruitsRecyclerViewAdapter extends RecyclerView.Adapter<FruitsViewHolder> {

    private List<FruitsData> allTheData;
    private Activity activity;

    public FruitsRecyclerViewAdapter(List<FruitsData> dataSet, Activity activity) {
        this.allTheData = dataSet;
        this.activity = activity;
    }

    public FruitsViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType){
        // Inflar el diseño de la vista del elemento de la lista.
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.fruits_view_holder, parent, false);
        return new FruitsViewHolder(view, allTheData); // Devolver un nuevo FruitsViewHolder.
    }

    public void onBindViewHolder(FruitsViewHolder holder, int position){
        // Obtener los datos para la posición específica y mostrarlos.
        FruitsData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    // Obtener el número total de elementos.
    public int getItemCount(){
        return allTheData.size();
    }
}
