package com.kennethmacharia.flashchatnewfirebase;

public class InstantMessage {
    // Model class representing an individual chat message

    private String message;
    private String author;

    // Args constructor
    public InstantMessage(String message, String author) {
        this.message = message;
        this.author = author;
    }

    // Firebase requires a non args condtructor for the class as well
    public InstantMessage() {
    }

    // Getters for the private class members
    public String getMessage() {
        return message;
    }

    public String getAuthor() {
        return author;
    }

}
