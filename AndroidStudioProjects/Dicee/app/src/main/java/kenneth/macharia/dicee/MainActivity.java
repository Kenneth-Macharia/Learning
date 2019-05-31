package kenneth.macharia.dicee;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

/*

- Create a variable of the type of view of interest
- Find the button view by it's id (in xml or in attributes window)

*/

        Button rollButton;
        rollButton = findViewById(R.id.rollButton);

        final ImageView leftDice = findViewById(R.id.image_leftDice);
        final ImageView rightDice = findViewById(R.id.image_rightDice);

/*

- Link listeners to the buttons to detect taps on the screen to the buttons.
- First part tells android studio we want to attach a listener to the view then we create a new
  listener class object, which comes complete with its action method.

*/

/*

- We want the dice images on our app to change with every roll.
- We have 6 images of the die, each each corresponding to a number between 1 and 6.
- We want to display a dice image based on the random number generated.
- To achieve this, we need to hold all the dice images in an array, then set the particular image
  view (left or right dice view) with the right dice image, based on the random number which will
  be used as the image array index.

  NB) - R class is an android generated class that contains numeric constants for all resources in a
        project. We can use this to refer to each resource by its location/name or id and it will return
        the numeric id of the resource.
      - The 'final' keyword makes a variable a constant thus once declared it will not change.
      - By making the array and the imageview variables final, we assure the on click event
        listener that these wont change so that they are always consistent and wont cause out of
        bound or reference errors.

*/

        final int [] diceArray = {
                R.drawable.dice1,
                R.drawable.dice2,
                R.drawable.dice3,
                R.drawable.dice4,
                R.drawable.dice5,
                R.drawable.dice6
        };

        rollButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

//          log.d(d means debug thus reporting in the logcat will be for debug messages)

                Log.d("Dicee", "The button has been clicked");

/*

Generate a random number and store it in a variable by first creating a random
number generator object from the Random class and using it to generate the random
number.

*/
                Random randomNumberGenerator = new Random();
                leftDice.setImageResource(diceArray[randomNumberGenerator.nextInt(6)]);
                rightDice.setImageResource(diceArray[randomNumberGenerator.nextInt(6)]);

            }
        });

    }
}
