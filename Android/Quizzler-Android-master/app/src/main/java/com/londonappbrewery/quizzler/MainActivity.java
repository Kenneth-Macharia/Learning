package com.londonappbrewery.quizzler;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.os.PersistableBundle;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import java.lang.reflect.Method;

public class MainActivity extends Activity {

    // Using the MVC design pattern, the xml will be the view, mainActivity will be the controller,
    // the TrueFalse class will be the model and an array will be the in-memory database of the
    // hardcoded string questions and answers.


    // TODO: Declare member variables here:
    Button mTrueButton;
    Button mFalseButton;
    TextView mTextViewQuestion;
    TextView mScoreTextView;
    ProgressBar mProgressBar;

    int mIndex = 0;
    int mQuestion;
    int mScore;


    // TODO: Uncomment to create question bank
   private TrueFalse[] mQuestionBank = new TrueFalse[] {
           new TrueFalse(R.string.question_1, true),
           new TrueFalse(R.string.question_2, true),
           new TrueFalse(R.string.question_3, true),
           new TrueFalse(R.string.question_4, true),
           new TrueFalse(R.string.question_5, true),
           new TrueFalse(R.string.question_6, false),
           new TrueFalse(R.string.question_7, true),
           new TrueFalse(R.string.question_8, false),
           new TrueFalse(R.string.question_9, true),
           new TrueFalse(R.string.question_10, true),
           new TrueFalse(R.string.question_11, false),
           new TrueFalse(R.string.question_12, false),
           new TrueFalse(R.string.question_13,true)
   };

    // TODO: Declare constants here
    // Math.ceil rounds up a decimal
    final int PROGRESS_BAR_INCREMENT = (int) Math.ceil(100.0/mQuestionBank.length);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // The onCreate savedInstanceState bundle will be null if the app has just be launched afresh,
        // and not if the app has a saved stated, i.e its activity was re-launched by screen rotation for example
        // If on relaunch, and having saved some state data, we can revert these values to smoothly revert
        // the app state as it was before.

        if (savedInstanceState != null) {
            mScore = savedInstanceState.getInt("ScoreKey");
            mIndex = savedInstanceState.getInt("IndexKey");

        } else {
            mScore = 0;
            mIndex = 0;
        }


       // Casting is converting one type to another, but only for types that are in the same objects
       // hierarchy (See Android dev guides for the object hierarchy for different components).
       //
       // Listeners can be set on any view component (check on Android dev guide).
       //
       // Callbacks are call to methods e.g when a click event is detected, then the onClick listener
       // invokes the onClick method which then runs the code required.


        mTrueButton = findViewById(R.id.true_button);
        mFalseButton = findViewById(R.id.false_button);

        mScoreTextView = findViewById(R.id.score);
        mProgressBar = findViewById(R.id.progress_bar);


        // Following the MVC pattern:
        // Retrieve the view (TextView) to display the questions

        mTextViewQuestion = findViewById(R.id.question_text_view);



        // To retrieve the questions to display, create an object of the model which represent the data.
        // This has already been done in the array, which has a new model object for each question resource.
        // To display any question, we just need to access its object in the array, use its object's
        // getter method to retrieve its resource id from the R class and pass that to the textView's
        // set method. This will be done in the updateQuestion method.


        //Update the app with saved state values on app re-launch
        mQuestion = mQuestionBank[mIndex].getQuestionID();
        mTextViewQuestion.setText(mQuestion);
        mProgressBar.incrementProgressBy(PROGRESS_BAR_INCREMENT);
        mScoreTextView.setText(String.format("Score %s/%s", mScore, mQuestionBank.length));


       // Method 1: Creating an explicit listener with a name and assigning a component to it.

        View.OnClickListener myListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                checkAnswer(true);
                updateQuestion();

            }
        };

        mTrueButton.setOnClickListener(myListener);

        //Method 2 for setting up an anonymous listener for a component. The listener in this case
        //is not explicitly defined, because it will not be used elsewhere.

        mFalseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                checkAnswer(false);
                updateQuestion();

            }
        });


    }

    private void updateQuestion () {
        mIndex = (mIndex + 1) % mQuestionBank.length;

        if (mIndex == 0) {
            //Create alert dialogue. 'this' refers to the current object, in this case the 'MainActivity'
            AlertDialog.Builder alert = new AlertDialog.Builder(this);

            // Set the alert contents
            alert.setTitle(R.string.alert_title);
            alert.setCancelable(false);
            alert.setMessage("Your score is: " + mScore + "points!");
            alert.setPositiveButton("Close Application", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialogInterface, int i) {
                    finish();
                }
            });
            alert.show();
        }

        mQuestion = mQuestionBank[mIndex].getQuestionID();
        mTextViewQuestion.setText(mQuestion);
        mProgressBar.incrementProgressBy(PROGRESS_BAR_INCREMENT);
        mScoreTextView.setText(String.format("Score %s/%s", mScore, mQuestionBank.length));

    }

    private void checkAnswer(Boolean userSelection) {

        // Get the corresponding question's answer
        boolean correctAnswer = mQuestionBank[mIndex].isAnswer();

        // Compare the correct answer to the answer selected by the user
        if (userSelection == correctAnswer) {
            //Display the appropriate toast message for the correct answer (Method 1)

            // Toast messages are used to quickly give used subtle info messages, which appear
            // are pop ups

            Toast myToast = Toast.makeText(getApplicationContext(), R.string.correct_toast,
                    Toast.LENGTH_SHORT);
            myToast.show();
            mScore +=1;

        } else {
            //Display the appropriate toast message for the correct answer (Method 2)
            Toast.makeText(getApplicationContext(), R.string.false_button, Toast.LENGTH_SHORT).show();

        }
    }

    @Override
    public void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);

        // Save app state variables here inside the Bundle called outState
        outState.putInt("ScoreKey", mScore);  //Save the current score
        outState.putInt("IndexKey", mIndex);  //Save the index of the current question's object

    }
}
