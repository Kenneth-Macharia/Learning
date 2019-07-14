package com.londonappbrewery.destini;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // TODO: Steps 4 & 8 - Declare member variables here:
    private TextView mTextView;
    private Button mTopButton;
    private Button mBottomButton;
    private int mStoryIndex = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // TODO: Step 5 - Wire up the 3 views from the layout to the member variables:
        mTextView = findViewById(R.id.storyTextView);
        mTopButton = findViewById(R.id.buttonTop);
        mBottomButton = findViewById(R.id.buttonBottom);

        // TODO: Steps 6, 7, & 9 - Set a listener on the top button:
        mTopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //From the story structure, this button will only ever trigger stories T3 and T6,
                // and will only take on T1ans1(default), T2ans1 and T3ans1

                // Story path logic
                if ((mStoryIndex == 1) || (mStoryIndex == 2)) {
                    mTextView.setText(R.string.T3_Story);
                    mTopButton.setText(R.string.T3_Ans1);
                    mBottomButton.setText(R.string.T3_Ans2);
                    mStoryIndex = 3;

                } else {
                    mTextView.setText(R.string.T6_End);
                    hideButtons();
                    mStoryIndex = 6;
                }

            }
        });

        // TODO: Steps 6, 7, & 9 - Set a listener on the bottom button:
        mBottomButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //From the story structure, this button will only ever trigger stories T2, T4 and
                // T5, and will only take on T1ans2(default), T2ans2 and T3ans2

                // Story path logic
                if (mStoryIndex == 1) {
                    mTextView.setText(R.string.T2_Story);
                    mTopButton.setText(R.string.T2_Ans1);
                    mBottomButton.setText(R.string.T2_Ans2);
                    mStoryIndex = 2;

                } else if (mStoryIndex == 2) {
                    mTextView.setText(R.string.T4_End);
                    hideButtons();
                    mStoryIndex = 4;

                } else {
                    mTextView.setText(R.string.T5_End);
                    hideButtons();
                    mStoryIndex = 5;
                }
            }
        });
    }

    protected void hideButtons () {
        mTopButton.setVisibility(View.GONE);
        mBottomButton.setVisibility(View.GONE);
    }

}
