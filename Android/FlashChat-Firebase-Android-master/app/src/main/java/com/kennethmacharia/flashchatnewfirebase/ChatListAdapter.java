package com.kennethmacharia.flashchatnewfirebase;

import android.app.Activity;
import android.content.Context;
import android.graphics.Color;
import android.text.TextUtils;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;

import java.util.ArrayList;

public class ChatListAdapter extends BaseAdapter {

    private Activity mActivity;
    private DatabaseReference mDatabaseReference;
    private String mDisplayName;
    private ArrayList<DataSnapshot> mSnapshotList;

    // DataSnashot is a Firebase data type for the data returned from the Firebase database.
    // ArrayList dynamic multi-storage Java data type unlike the Array which is fixed length.

    // Messages coming from the Firebase database will be stored in the DataSnapshot arraylist. This
    // when new messgaes are uploaded the cloud database. A Firebase ChildEventListener looks out for changes in the database and reports back to the arraylist when the changes are detected e.g messages added

    private ChildEventListener mListener = new ChildEventListener() {
        @Override
        public void onChildAdded(DataSnapshot dataSnapshot, String s) {
            // Implementing the child/msg added call back method. When a mesg is added, a datasnapshot object is sent back in JSON form, this is where we will the data received

            // Each time a new msg is added, the msg is send back to the app, from where we add it to the list of messages already received, ready to display them

            mSnapshotList.add(dataSnapshot);

            // Refresh the list view with new availble info
            notifyDataSetChanged();

        }

        @Override
        public void onChildChanged(DataSnapshot dataSnapshot, String s) {

        }

        @Override
        public void onChildRemoved(DataSnapshot dataSnapshot) {

        }

        @Override
        public void onChildMoved(DataSnapshot dataSnapshot, String s) {

        }

        @Override
        public void onCancelled(DatabaseError databaseError) {

        }
    };


    ChatListAdapter (Activity activity, DatabaseReference ref, String name) {
        mActivity = activity;
        mDatabaseReference= ref.child("messages");
        mDatabaseReference.addChildEventListener(mListener);  // Attach firebase listener to our specific dbase object
        mDisplayName = name;
        mSnapshotList = new ArrayList<>();
    }

    // Create an inner class to retrieve and hold the views in a single chat message row as well as
    // their display parameters
    static class ViewHolder {
        TextView authName;
        TextView body;
        LinearLayout.LayoutParams params;  // Holds the display layout for the chat message rows
    }

    @Override
    public int getCount() {
        // The listView will ask the arrayadapter how many chat items it has and the arrayadapter will return the number via this getCount method
        return mSnapshotList.size();
    }

    @Override
    public InstantMessage getItem(int position) {
        // Get the relavant/correct snapshot from the arraylist i.e the correct msg data by passing in an index of the required snapshot

        DataSnapshot snapshot = mSnapshotList.get(position);

        // Return the instnat message from the retireved snapshot instant and return it
        return snapshot.getValue(InstantMessage.class);
    }

    @Override
    public long getItemId(int position) {
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // This method return a chat view row object populated with the data we want i.e messgae
        // author and message text.
        // Since we cna have numerous chat messages and can only display a few at a time, the this
        // method will attempt to recycle row that are no longer displayed and just update thier data,
        // instead of creating new chat view rows which is computationaly intensive. So it creates new
        // chat view rows only if there are no available chat view rows to reuse.

        if (convertView == null) {
            // Get a new row from the chat msg rows xml file, ie. create a new row
            LayoutInflater inflater = (LayoutInflater) mActivity.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.chat_msg_row, parent, false);

            // Instantiate the view holder inner class
            final ViewHolder holder = new ViewHolder();

            // Populate the ViewHolder object with the required chat message row views
            holder.authName = convertView.findViewById(R.id.author);
            holder.body = convertView.findViewById(R.id.message);
            holder.params = (LinearLayout.LayoutParams) holder.authName.getLayoutParams();
            convertView.setTag(holder);    // Save the newly created chat view row to use later

            // convertview reps a list item in the arraylist
        }

        // If there are chat row to reuse, display the correct message;
        // Get the current message to be displayed from the Arraylist
        final InstantMessage message = getItem(position);

        // Fetch the chat message row view that was saved in the convert  view earlier
        final ViewHolder holder = (ViewHolder) convertView.getTag();

        // check if the message author is the same as the display name in the view holder and return true or false
        boolean isMe = message.getAuthor().equals(mDisplayName);
        setChatRowAppearance(isMe, holder);  // For message formatting

        // Refresh the data that is in the message view from the last time it  was used
        String author = message.getAuthor();
        holder.authName.setText(author);

        String msg = message.getMessage();
        holder.body.setText(msg);

        return convertView;
    }

    public void cleanUp() {
        // Method to stop the app checking for database updates when it isno longer active
        mDatabaseReference.removeEventListener(mListener);
    }

    // Method to ensure that messages are properly formated
    private void setChatRowAppearance(boolean isItMe, ViewHolder holder) {
    // If messages are from me, align then right else and make the author text green, else align them left and make the author text color blue.

        if (isItMe) {
            holder.params.gravity = Gravity.END;
            holder.body.setBackgroundResource(R.drawable.bubble2);
        } else {
            holder.params.gravity = Gravity.START;
            holder.authName.setTextColor(Color.BLUE);
            holder.body.setBackgroundResource(R.drawable.bubble1);
        }

        holder.authName.setLayoutParams(holder.params);
        holder.body.setLayoutParams(holder.params);
    }

}
