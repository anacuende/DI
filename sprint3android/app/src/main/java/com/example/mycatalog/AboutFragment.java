package com.example.mycatalog.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.fragment.app.Fragment;
import com.example.mycatalog.R;
import android.widget.TextView;

public class AboutFragment extends Fragment {

    public AboutFragment() {
        // Required empty public constructor
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_about, container, false);

        // Encuentra el TextView en el diseño y establece su contenido
        TextView textView = rootView.findViewById(R.id.aboutContentTextView);
        textView.setText(getString(R.string.about_content));

        return rootView;
    }
}
