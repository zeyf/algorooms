// Module imports
import React, { useContext, useEffect } from 'react';

// Component imports
import RoomMember from './RoomMember';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { useMutation, useOthers, useSelf, useStorage } from '../../../../../../../../liveblocks.config';
import { toast } from 'react-toastify';
import createUID from '@/utilities/createUID';
import axios from 'axios';
import buildRoute from '@/utilities/buildRoute';
import { LiveList, LiveObject } from '@liveblocks/client';
import languageMapper, { languageMap } from '@/utilities/languageMapper';

export default ({

}) => {





  // Get the name of the room
  const {
    name
  } = useContext(RoomContext);





  // Get round playing status to use for conditional rendering and prevention of room state manipulation while true
  const inRound = useStorage(r => r.inRound);

  // Get the current host for conditional rendering of start round button
  const host = useStorage(r => r.host);

  // Get all questions for "paginated" fetching on round start
  const questionUIDs = useStorage(r => r.questions);
  
  // Get awaitingQuestion status for conditional rendering and prevention of room state manpulation while true
  const awaitingQuestion = useStorage(r => r.awaitingQuestion);

  // Get self presence
  const myPresence = useSelf(me => me.presence);

  
  // Get others' presences
  const others = useOthers();
  
  // Make list of all members including self
  const members = [
    myPresence,
    ...others.map((other) => other.presence)
  ];

  // Get self username
  const username = myPresence.username;

  // Checks if all questions are completed
  const completedQuestions = questionUIDs.length === 0;





  // Performs mutation on the room storage
  const nextQuestion = useMutation(async ({ storage }, langMapper = languageMapper) => {

    // Change status to let all users know a question is being awaited
    storage.set("awaitingQuestion", true);
    
    // Get the LiveList of questions
    const questions = storage.get("questions");
    
    // Get the next question
    const nextQuestionUID = questions.get(questions.length - 1);

    // Delete the last question from the LiveList in order to "move on"
    questions.delete(questions.length - 1);
  
    // Make a request to get the next question by UID
    const response = await axios.get(buildRoute(`/api/questions/verify/${nextQuestionUID}`)).then(r => r).then(r => r.data);
    
    // Reset the editor texts for the supported languages
    const newEditorTextsObject:any = {  };

    // Populate and declare blank language editor texts for all supported languages
    for (const language of Object.keys(langMapper))
      newEditorTextsObject[language] = "";

    // Reset the LiveObject<EditorTexts> for the supported languages
    storage.set("editorTexts", new LiveObject(newEditorTextsObject));

    // Set the current question
    storage.set("currentQuestion", response.question);

    // Change status to let all users know a question is not being awaited anymore
    storage.set("awaitingQuestion", false);

    // Change status to start the round
    storage.set("inRound", true);

  }, [  ]);

  const repopulateQuestions = useMutation(async ({ storage }, langMapper = languageMapper) => {

    // Change status to let all users know a question is being awaited
    storage.set("awaitingQuestion", true);

    // Get the current difficulty setting
    const difficulty = storage.get("difficulty");

    // Get the current topics setting
    const topics = storage.get("topics").toArray();

    // Make a request to get all questions by UID as per the difficulty and topics settings
    const allQuestionsResponse = await axios.post(buildRoute("/api/questions/filter"), {
      difficulty,
      topics
    }).then(r => r).then(r => r.data);

    
    // If we did not find any quesstions based on the current difficulty and topics settings
    if (!allQuestionsResponse.exists) {
      
      // Change status to let all users know a question is not being awaited anymore
      storage.set("awaitingQuestion", false);
      
      // Return false to signify it was not possible to repopulate questions
      return false;
    };

    // Get the next question
    const nextQuestionUID = allQuestionsResponse.questions.pop();

    // Set the storage to be of the new questions
    storage.set("questions", new LiveList<string>(allQuestionsResponse.questions));

    // Make a request to get the next question by UID
    const questionResponse = await axios.get(buildRoute(`/api/questions/verify/${nextQuestionUID}`)).then(r => r).then(r => r.data);

    // Reset the editor texts for the supported languages
    const newEditorTextsObject:any = {  };

    // Populate and declare blank language editor texts for all supported languages
    for (const language of Object.keys(langMapper))
      newEditorTextsObject[language] = "";

    // Reset the LiveObject<EditorTexts> for the supported languages
    storage.set("editorTexts", new LiveObject(newEditorTextsObject));

    // Set the current question
    storage.set("currentQuestion", questionResponse.question);

    // Change status to let all users know a question is not being awaited anymore
    storage.set("awaitingQuestion", false);

    // Change status to start the round
    storage.set("inRound", true);

  }, [  ]);





  return (
    <section className="flex-1 flex flex-col bg-darkAccent p-5 box-border">
      <span className="text-white uppercase text-xl">{ name }</span>
      <span className="py-6 font-bold text-white">ROOM MEMBERS</span>
      <div className="flex flex-wrap gap-2">
        {

          // Display all room members

          members.map(member =>
            <RoomMember { ...member } key={createUID()} />
          )
        }
      </div>

        {
        
          // Only the host will have access to the start round button
          host === username &&

          <button
            className={`${inRound ? "opacity-50" : ""} px-8 py-2 rounded-xl my-4 font-bold bg-greenAccent`}
            
            // Disable when in round or awaiting a question
            disabled={inRound || awaitingQuestion}
            
            onClick={() => {

              // NOTE: add condition for if no changes have been made to the settings like topics and difficulty

              // If we have NOT completed all questions, start a new round
              if (!completedQuestions)
                nextQuestion();

              // Otherwise if we have completed all questions, toast and repopulate questions
              else {
                toast("All questions completed! Starting round based on current difficulty and topics settings.");
                repopulateQuestions()
                // If we are not in a round, that mean there is no questions found
                 if(!inRound){
                  toast("No questions with suitable difficulty and topics");
                 }
              };

            }}
          >
          START ROUND
        </button>
        }

    </section>
  );





};
