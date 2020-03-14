package com.kennethmacharia.flashchatnewfirebase;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.security.PrivateKey;


public class MainChatActivity extends AppCompatActivity {

    // TODO: Add member variables here:
    private String mDisplayName;
    private ListView mChatListView;
    private EditText mInputText;
    private ImageButton mSendButton;
    private DatabaseReference mDatabaseReference;
    private ChatListAdapter mAdapter;   // ChatListAdapter class object variable

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_chat);

        // TODO: Set up the display name and get the Firebase reference object
        setdisplayName();

        // A DatabaseReference object refers to a particular cloud location, where our data will be stored
        mDatabaseReference = FirebaseDatabase.getInstance().getReference();

        // Link the Views in the layout to the Java code
        mInputText = findViewById(R.id.messageInput);
        mSendButton = findViewById(R.id.sendButton);
        mChatListView = findViewById(R.id.chat_list_view);

        // TODO: Send the message when the "enter" button is pressed
        mInputText.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView textView, int i, KeyEvent keyEvent) {
                sendMessage();
                return true; // Always change to true when the event is handled
            }
        });

        // TODO: Add an OnClickListener to the sendButton to send a message
        mSendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                sendMessage();
            }
        });

    }

    // TODO: Retrieve the display name from the Shared Preferences
    private void setdisplayName() {
        // SharedPreferences prefs = getSharedPreferences(RegisterActivity.CHAT_PREFS, MODE_PRIVATE);
        // mDisplayName = prefs.getString(RegisterActivity.DISPLAY_NAME_KEY, null);
        //
        // if (mDisplayName == null) mDisplayName = "Anonymous";

        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        mDisplayName = user.getDisplayName();
    }


    private void sendMessage() {

        // TODO: Grab the text the user typed in and push the message to Firebase

        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();

        if (user != null) {
            Log.d("FlashChat", "User: " + user.getUid());
        }

        String input = mInputText.getText().toString();

        // Check the user did not send an empty message
        if (!input.equals("")) {

            Log.d("FlashChat", "Msg: " + input);

            // Initialize the InstaMNessage class to get a message object
            InstantMessage chat = new InstantMessage(input, mDisplayName);

            /*
            Use the DatabaseReference object to persist a chat message to Firebase
            DatabaseReference object = locations on Firebase to store our data
            child() gets a specific location for storing and names it <args>
            put() gets a reference to the location from child()
            setValue() store the message passed to it to the location from put()
            */

            // mDatabaseReference.child("messages").push().setValue(chat);
            // https://flashchatandroid-49de3.firebaseio.com
            mDatabaseReference.child("messages").push().setValue(chat);

            // Clear message input box after message has been sent
            mInputText.setText("");

        }
    }


    // TODO: Override the onStart() lifecycle method. Setup the adapter here.
    @Override
    public void onStart() {
        super.onStart();
        // Instanttiate the ChalistAdapter class
        mAdapter = new ChatListAdapter(this, mDatabaseReference, mDisplayName);

        // Connect the chat list view to the right adapter (ChatListAdapter)
        // (NB) The adapter is required as a middleman between the list view which displays the chat messages and the chat message data source i.e the ArrayList which hold the mesage object from the Firebase database
        mChatListView.setAdapter(mAdapter);

    }


    @Override
    public void onStop() {
        super.onStop();

        // TODO: Remove the Firebase event listener on the adapter.
        // (NB) always free up phone resources when the appis no longer active, this can be done in this method.
        mAdapter.cleanUp();

    }

}
