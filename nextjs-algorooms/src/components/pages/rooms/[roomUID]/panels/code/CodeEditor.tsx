// Module imports
import CodeMirror from '@uiw/react-codemirror';
import { sublime } from '@uiw/codemirror-theme-sublime'
import languageMapper from '@/utilities/languageMapper';

// Interface imports
import { useMutation, useOthers, useSelf, useStorage, useUpdateMyPresence } from '../../../../../../../liveblocks.config';
import { EditorState } from '@codemirror/state';
import {Tooltip, showTooltip, EditorView} from "@codemirror/view"
import {StateField} from "@codemirror/state"

import Split from 'react-split';
import CodeTester from './CodeTester';



const CodeEditor = ({

}) => {

    // Get the current editor language
    const editorLanguage = useStorage(({ language }) => language);

    // Get the current editor text based on what the current language is
    const editorText = useStorage(({ editorTexts }) => editorTexts)[editorLanguage];

    // Get the LiveObject<EditorTexts> and set the specific language's editor text to the newEditorText onChange
    const handleEditorTextEdit = useMutation(({ storage }, newEditorText, editorLanguage) => {
        storage.get("editorTexts").set(editorLanguage.toLowerCase(), newEditorText);
    }, [  ]);

    // Get self presence
    const myPresence = useSelf(me => me.presence);
    
    // Get others' presence
    const others = useOthers();
    
    // Used to handle presence update for text editor position
    // NOTE: This is NOT supporting cursors across the different language editor texts
    // NOTE: On language change, the editor position defaults back to 0 for all users
    // This will be a Nice-To-Have change
    const handleEditorPositionUpdate = useUpdateMyPresence();

    // This function will get all other users' tooltips and create the DOM elements for them
    const getCursorTooltips = (state: EditorState): readonly Tooltip[] => {

        // Get all other user tooltips
        const otherTooltips = others.map(other => {
            return {
                cursorLocationData: other.presence.cursorLocationData,
                username: other.presence.username,
                color: other.presence.color
            }
        });

        // Get self tooltip
        const myTooltip = {
            cursorLocationData: myPresence.cursorLocationData,
            username: myPresence.username,
            color: myPresence.color
        };

        // Return the formatted tooltips with the user information like username and color
        return [
            ...otherTooltips
        ]
          // Only give tooltips to users that are at one location [start, end] where start = end, not selecting text
          .filter((userTooltipState) => userTooltipState.cursorLocationData.empty)
          // 
          .map((userTooltipState) => {
        
            // Return a list of dom elements for the tooltips with proper positioning, styling, and content
            return {

                pos: userTooltipState.cursorLocationData.head,
                above: true,
                strictSide: true,
                arrow: true,

                // Creates the DOM elements
                create: () => {
                    let dom = document.createElement("div")
                    dom.className = "cm-tooltip-cursor"
                    dom.textContent = userTooltipState.username;
                    dom.style.backgroundColor = userTooltipState.color;

                    return { dom };
                }

            };

          });
      };
    
      // Function to provide updates to the editor state for cursor tooltips
      const cursorTooltipField = StateField.define<readonly Tooltip[]>({

        // Creates the tooltips
        create: getCursorTooltips,
      
        // Performs updates on the editor based on the tooltips
        update(tooltips, tr) {
            
            // If there is no change and no selection on the document, return the tooltips
            if (!tr.docChanged && !tr.selection)
                return tooltips;
            
            // If there are changes to the doc, or there is selection, or anything else happening, show the cursor tooltips based on current state
            else
                return getCursorTooltips(tr.state);
        },
      
        // Will display the tooltips
        provide: f => showTooltip.computeN([f], state => state.field(f))
      })

      // Create general styling for all tooltips that will be displayed
      const cursorTooltipBaseTheme = EditorView.theme({

        ".cm-tooltip.cm-tooltip-cursor": {
            
            "& .cm-tooltip-arrow:before": {
                borderTopColor: "white"
            },

            "& .cm-tooltip-arrow:after": {
                borderTopColor: "transparent"
            },
        
            color: "white",
            border: "none",
            padding: "2px 7px",
            borderRadius: "4px"

        },

        ".ͼba .cm-cursor, .cm-dropCursor": {
            borderLeftColor: myPresence.color,
            backgroundColor: myPresence.color,
            borderColor: myPresence.color
        },

        ".ͼba .cm-content": {
            caretColor: myPresence.color
        }

      });

    console.log(editorLanguage)
    console.log(languageMapper[editorLanguage])
    return (
        <div className="w-[822px] h-[579px]">
            <div className="rounded-lg overflow-hidden w-[822px] h-[579px] mt-5">
                <Split>
                    <CodeMirror

                        // Stores the theme for the text editor
                        theme={sublime}

                        // Stores the text of the editor based on the current language
                        value={editorText}

                        // Stores the different extensions for the CodeMirror editor
                        extensions={[
                            
                            // Get the syntax highlighting for the specific language selected
                            languageMapper[editorLanguage].syntaxHighlightingExtension(),

                            // Creates the tooltip
                            cursorTooltipField,

                            // Styles the tooltip
                            cursorTooltipBaseTheme
                        ]}

                        // Changes made upon every possible update of the editor state
                        onUpdate={viewUpdate => {

                            // Get the current ranges of a given user and their own selection
                            const currentData = viewUpdate.state.selection.ranges[0];

                            // If there is an update either on the start or on the end of the selection range
                            if (myPresence.cursorLocationData.from !== currentData.from || myPresence.cursorLocationData.to !== currentData.to) {

                                // Update the current user's position in their presence -- in order to update it across clients
                                handleEditorPositionUpdate({
                                    ...myPresence,
                                    cursorLocationData: {
                                        ...currentData,

                                        // This information is not passed via spread operator due to private variables, must explicitly define

                                        // Whether or not [start, end] or [from, to] is a range of length = 0
                                        empty: currentData.empty,

                                        // Get the lowest and rightmost position of the selection, there for the "to" or "end" location
                                        head: currentData.head
                                    }
                                });

                            }
                        }}

                        // Handle text editor changes and map it to the specific editor language that is currently selected
                        onChange={(e) => {
                            handleEditorTextEdit(e, editorLanguage);
                        }}

                        height="579px"
                        width="822px"

                        // An attempt to style the cursor color for a given client
                        style={{
                            borderLeft: "1px",
                            borderLeftColor: myPresence.color,
                            background: myPresence.color
                        }}
                    />
                    
                    <CodeTester />
                </Split>
            </div>

        </div>
    );

};

export default CodeEditor;