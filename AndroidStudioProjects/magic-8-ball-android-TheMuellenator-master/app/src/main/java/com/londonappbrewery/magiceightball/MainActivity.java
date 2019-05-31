package com.londonappbrewery.magiceightball;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.lang.reflect.Array;
import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Button ask_button = findViewById(R.id.askButton);
        final ImageView ball_img = findViewById(R.id.imageView);

        final int [] image_array = new int[]{
                R.drawable.ask_again,
                R.drawable.cannot_tell_now,
                R.drawable.go_for_it,
                R.drawable.no,
                R.drawable.wait_for_it
        };

        ask_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Random randomNumber = new Random();
                ball_img.setImageResource(image_array[randomNumber.nextInt(4)]);
            }
        });

    }
}
