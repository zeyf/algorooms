// Module imports
import { useState, useRef, useEffect, useContext } from 'react';
import CodeMirror, { ReactCodeMirrorRef } from '@uiw/react-codemirror';
import { javascript as JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-javascript';
import { python as PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-python';
import { cpp as CPP_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-cpp';
import { java as JAVA_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-java';
import { sublime } from '@uiw/codemirror-theme-sublime';
import * as Y from 'yjs';
import { WebrtcProvider } from 'y-webrtc';
import { yCollab } from 'y-codemirror.next';

// Interface imports
import { codeEditorInterface } from './Interfaces';
import { countReset } from 'console';
import rooms from '@/pages/rooms';
import { RoomContext } from '@/contexts/RoomContextLayer';
import { AppUserContext } from '@/contexts/AppUserContextLayer';
import {
  useMutation,
  useOthers,
  useSelf,
  useStorage,
  useUpdateMyPresence,
} from '../../../../../../../liveblocks.config';
import { EditorState } from '@codemirror/state';
import { Tooltip, showTooltip, EditorView } from '@codemirror/view';
import { StateField } from '@codemirror/state';

const CodeEditor = ({}: codeEditorInterface) => {
  const { socket, uid, code, setCode, language } = useContext(RoomContext);

  const { username } = useContext(AppUserContext);

  const editorText = useStorage(({ editorText }) => editorText) || '';

  const languageMapping = [
    ['python', PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION],
    ['javascript', JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION],
    ['cpp', CPP_SYNTAX_HIGHLIGHTING_EXTENSION],
    ['java', JAVA_SYNTAX_HIGHLIGHTING_EXTENSION],
  ];

  const codeMirrorRefs = useRef<ReactCodeMirrorRef>({});

  const handleEditorTextEdit = useMutation(({ storage }, newEditorText) => {
    storage.set('editorText', newEditorText);
  }, []);

  const myPresence = useSelf((me) => me.presence);

  const others = useOthers();

  const handleEditorPositionUpdate = useUpdateMyPresence();

  function getCursorTooltips(state: EditorState): readonly Tooltip[] {
    const otherTooltips = others.map((other) => {
      return {
        cursorLocationData: other.presence.cursorLocationData,
        username: other.presence.username,
        color: other.presence.color,
      };
    });

    const myTooltip = {
      cursorLocationData: myPresence.cursorLocationData,
      username: myPresence.username,
      color: myPresence.color,
    };

    return [
      ...otherTooltips,
      // myTooltip
    ]
      .filter((userTooltipState) => userTooltipState.cursorLocationData.empty)
      .map((userTooltipState) => {
        // let line = state.doc.lineAt(range.head);

        return {
          pos: userTooltipState.cursorLocationData.head,
          above: true,
          strictSide: true,
          arrow: true,
          create: () => {
            let dom = document.createElement('div');
            dom.className = 'cm-tooltip-cursor';
            dom.textContent = userTooltipState.username;
            dom.style.backgroundColor = userTooltipState.color;

            return {
              dom,
            };
          },
        };
      });
  }

  const cursorTooltipField = StateField.define<readonly Tooltip[]>({
    create: getCursorTooltips,

    update(tooltips, tr) {
      if (!tr.docChanged && !tr.selection) return tooltips;
      return getCursorTooltips(tr.state);
    },

    provide: (f) => showTooltip.computeN([f], (state) => state.field(f)),
  });

  const cursorTooltipBaseTheme = EditorView.theme({
    '.cm-tooltip.cm-tooltip-cursor': {
      //   backgroundColor: c,
      color: 'white',
      border: 'none',
      padding: '2px 7px',
      borderRadius: '4px',
      '& .cm-tooltip-arrow:before': {
        borderTopColor: 'white',
      },
      '& .cm-tooltip-arrow:after': {
        borderTopColor: 'transparent',
      },
    },
  });

  // Focus on the editor if empty line is clicked
  const handleEditorClick = (e: React.MouseEvent<HTMLDivElement>) => {
    if (e.target === e.currentTarget) {
      codeMirrorRefs.current.view.focus();
    }
  }

  return (
    <div className="w-full h-full">
      <div className="rounded-lg overflow-auto w-full h-full bg-[#303841] relative z-1" onClick={handleEditorClick}>
        <CodeMirror
          ref={codeMirrorRefs}
          height="100%"
          style={{
            borderLeft: '1px',
            borderLeftColor: myPresence.color,
            background: myPresence.color,
          }}
          theme={sublime}
          value={editorText}
          extensions={[
            ...languageMapping
              .filter(([lang, ext]: any[]) => language === lang)
              .map(([lang, ext]: any[]) => ext()),
            cursorTooltipField,
            cursorTooltipBaseTheme,
          ]}
          onUpdate={(viewUpdate) => {
            const currentData = viewUpdate.state.selection.ranges[0];

            if (
              myPresence.cursorLocationData.from !== currentData.from ||
              myPresence.cursorLocationData.to !== currentData.to
            ) {
              handleEditorPositionUpdate({
                ...myPresence,
                cursorLocationData: {
                  ...currentData,
                  empty: currentData.empty,
                  head: currentData.head,
                },
              });
            }
          }}
          onChange={handleEditorTextEdit}
        />
      </div>
    </div>
  );
};

export default CodeEditor;
