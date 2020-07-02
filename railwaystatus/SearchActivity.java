package com.root.railwaystatus;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class SearchActivity extends AppCompatActivity {

    /*@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);
        final EditText editText;
        Button button;
        @Override
        protected void onCreate (Bundle savedInstanceState){
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_search);
            editText = (EditText) findViewById(R.id.editText);
            button = (Button) findViewById(R.id.button);*/

    EditText editText;
    Button button;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);
        editText=(EditText)findViewById(R.id.editText);
        button=(Button)findViewById(R.id.button);

            button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (editText.length() < 5) {
                        Toast.makeText(getApplicationContext(), " Train No. Incorrect. ", Toast.LENGTH_SHORT).show();
                    } else {
                        String train = String.valueOf(editText.getText().toString());
                        Intent intent = new Intent(getApplicationContext(), Display.class);
                        intent.putExtra("train", train);
                        startActivity(intent);
                    }
                }
            });
        }
    }



