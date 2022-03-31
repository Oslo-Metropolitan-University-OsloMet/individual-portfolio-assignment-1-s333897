import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Bots extends JFrame{
    private JTextArea ChatArea = new JTextArea();
    private JTextField ChatBox = new JTextField();

    //Setting the max amount for the random number generator.
    int min = 0;
    int max = 2;
    //I made some premade lits if "Things to do", which later on decides how the bots will respond
    String [] listOfThings = {"food","cry","ice cream","walk","jog","run","hike"};
    String [] listOfVerbs = {"crying","walking","swimming","running","biking","hiking","climbing"};

    private boolean foundVerbBoolean = false;
    private boolean FoundBadVerbBoolean = false;

    public Bots () {
        //Basic set-up for a window where you can talk to the bots
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setLayout(null);
        frame.setSize(600, 800);
        frame.setTitle("Chat Bot");
        frame.add(ChatArea);
        frame.add(ChatBox);
        //For text area
        ChatArea.setSize(570,600);
        ChatArea.setLocation(4,2);

        //For text field
        ChatBox.setSize(570,30);
        ChatBox.setLocation(4, 700);

        ChatBox.addActionListener(new ActionListener() {
            @Override
            //This are the instructions for how the bots respond
            public void actionPerformed(ActionEvent e) {
                String gtext = ChatBox.getText();
                String verb = "";
                String object = "";
                ChatArea.append("Me: " + gtext + "\n");
                ChatBox.setText("");

                //Decides if the verd ends with "ing" and creates different responses
                for (String listOfThing : listOfThings) {
                    if (gtext.contains(listOfThing)) {
                        foundVerbBoolean = false;
                        object = listOfThing;
                    }
                }
                for (String listOfVerb : listOfVerbs) {
                    if (gtext.contains(listOfVerb)) {
                        foundVerbBoolean = true;
                        verb = listOfVerb;
                    }
                }


                if (gtext.contains("Hi") || gtext.contains("Hello") || gtext.contains("hello")){
                    //Basic response to a greeting with 3 options. These are randomized
                    String greetingAndrew [] = {"Hello!", "Yo!", "What's up?"};
                    String greetingCharlie [] = {"Hi!", "Sup?", "Hey buddy"};
                    String greetingSofia [] = {"Hiiii!", "Look who showed up :P", "The gang is here!"};
                    String greetingKaren [] = {"Finally...", "Always the latest to join", "What took you so long?"};

                    //Randomizing the answer the bots will give. This way the bots will almost never give the same
                    // combination of answers.
                    int random_int1 = (int) Math.floor(Math.random()*(max-min+1)+min);
                    int random_int2 = (int) Math.floor(Math.random()*(max-min+1)+min);
                    int random_int3 = (int) Math.floor(Math.random()*(max-min+1)+min);
                    int random_int4 = (int) Math.floor(Math.random()*(max-min+1)+min);

                    //Printing the bots answer in the chat window.
                    botAdrew(greetingAndrew[random_int1]);
                    botCharlie(greetingCharlie[random_int2]);
                    botSofia(greetingSofia[random_int3]);
                    botKaren(greetingKaren[random_int4]);
                }

                else if (gtext.contains("How are you") || gtext.contains("How's life")) {
                    //Same thing as the last if-sentence, the only difference is a respons to how they are feeiling
                    String feelingAndrew [] = {"I'm doing fine!", "Not great :/", "I'm alright"};
                    String feelingCharlie [] = {"Could be better", "Good enough i guess", "Better than usual"};
                    String feelingSofia [] = {"I'm grrrrreat!", "Better now you are here ;)", "Feeling a little blue " +
                            ":("};
                    String feelingKaren [] = {"Stop pretending like you care", "Why do you ask huh?", "None of your " +
                            "business"};

                    int random_int1 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int2 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int3 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int4 = (int) Math.floor(Math.random() * (max - min + 1) + min);

                    botAdrew(feelingAndrew[random_int1]);
                    botCharlie(feelingCharlie[random_int2]);
                    botSofia(feelingSofia[random_int3]);
                    botKaren(feelingKaren[random_int4]);
                }

                else if ((gtext.contains("Let's") || gtext.contains("let's") || gtext.contains("How about we") || gtext.contains("What if we")) && !foundVerbBoolean) {
                    //These are the instructions if the verb does not end with "ing". If the sentence structure isn't
                    // differentiated, the bots would have a weird awnser.
                    String DoSomeThingAndrew[] = {"I'm not really in the mood for " +object, object+" sounds amazing " +
                            "right now!", "I could go for some "+object};
                    String DoSomeThingCharlie[] = {"You always want to " +object, "Got nothing better to do",
                            "Pretty sure that place is closed right now"};
                    String DoSomeThingSofia[] = {"Do you only think about " +object, object+"? eeh why not.",
                            object+ " TIME!"};
                    String DoSomeThingKaren[] = {"Why are you like this...", object+" sounds amazing, if you don't " +
                            "have to come", "I'm busy"};

                    int random_int1 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int2 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int3 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int4 = (int) Math.floor(Math.random() * (max - min + 1) + min);

                    botAdrew(DoSomeThingAndrew[random_int1]);
                    botCharlie(DoSomeThingCharlie[random_int2]);
                    botSofia(DoSomeThingSofia[random_int3]);
                    botKaren(DoSomeThingKaren[random_int4]);
                }

               else if (foundVerbBoolean){
                    //If foundVerbBoolean is true, then that must mean the user is asking the bots to do something.
                    //By doing this, the response seems more natural
                    String DoAThingAndrew[] = {"I'm not really in the mood for " +verb, verb +
                            " sounds amazing right now!", "I could go for some "+verb};
                    String DoAThingCharlie[] = {"You always want to go " +verb, "Got nothing better to do",
                            "It's not really the weather for it"};
                    String DoAThingSofia[] = {"Again with your "+verb, "Do we have to?", "YESS! LET'S GO "+verb};
                    String DoAThingKaren[] = {"You always have the worst suggestions", "How about someone else " +
                            "decides what we do for once?", "Fine... "+verb +" sounds alright i guess"};

                    int random_int1 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int2 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int3 = (int) Math.floor(Math.random() * (max - min + 1) + min);
                    int random_int4 = (int) Math.floor(Math.random() * (max - min + 1) + min);

                    botAdrew(DoAThingAndrew[random_int1]);
                    botCharlie(DoAThingCharlie[random_int2]);
                    botSofia(DoAThingSofia[random_int3]);
                    botKaren(DoAThingKaren[random_int4]);
                }

                else if (gtext.contains("what day") || gtext.contains("What day")){
                    //Using a computer to ask what day it is doesn't really make sense since you can look it up easily.
                    //There for I wanted every bot to ridicule the asker, and I don't feel they need a lot of responses.
                    String dayAndrew [] = {"Come on man..."};
                    String dayCharlie [] = {"Are you serious right now?"};
                    String daySofia [] = {"You know every computer has a calender right?"};
                    String dayKaren [] = {"You might be the dumbest person i know..."};

                    botAdrew(dayAndrew[0]);
                    botCharlie(dayCharlie[0]);
                    botSofia(daySofia[0]);
                    botKaren(dayKaren[0]);
                }

                //Could add more responses to different questions, but they would look similar to the ones above.
                //This is a simple code that can create chatbots without needing to download templates or resources
                //from the internet. Even tho this might not be as efficient, it's a simple beginning.

            }
        });

    }
    private void botAdrew(String string){
        ChatArea.append("Andrew: " + string + "\n");
    }
    private void botCharlie(String string){
        ChatArea.append("Charlie: " + string + "\n");
    }
    private void botSofia(String string){
        ChatArea.append("Sofia: " + string + "\n");
    }
    private void botKaren(String string){
        ChatArea.append("Karen: " + string + "\n");
    }


    public static void main(String [] args){
        new Bots();
    }
}
