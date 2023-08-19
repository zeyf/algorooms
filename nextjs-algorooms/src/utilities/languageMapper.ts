import { javascript as JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-javascript';
import { python as PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION } from "@codemirror/lang-python";
// import { cpp as CPP_SYNTAX_HIGHLIGHTING_EXTENSION } from "@codemirror/lang-cpp";
// import { java as JAVA_SYNTAX_HIGHLIGHTING_EXTENSION } from '@codemirror/lang-java';

export type languageMap = {
    syntaxHighlightingExtension: Function,
    jDoodleAPITemplateConfiguration: {
        language: string,
        version: string,
        compileOnly: boolean
    }
};

export default {

    "javascript": {
        syntaxHighlightingExtension: JAVASCRIPT_SYNTAX_HIGHLIGHTING_EXTENSION,
        jDoodleAPITemplateConfiguration: {
            language: "nodejs",
            version: "4",
            compileOnly: false
        }
    },

    "python": {
        syntaxHighlightingExtension: PYTHON_SYNTAX_HIGHLIGHTING_EXTENSION,
        jDoodleAPITemplateConfiguration: {
            language: "python3",
            version: "4",
            compileOnly: false
        }
    },

    // "cpp": {
    //     syntaxHighlightingExtension: CPP_SYNTAX_HIGHLIGHTING_EXTENSION,
    //     jDoodleAPITemplateConfiguration: {
    //         language: "cpp17",
    //         version: "1",
    //         compileOnly: false
    //     }
    // },

    // "java": {
    //     syntaxHighlightingExtension: JAVA_SYNTAX_HIGHLIGHTING_EXTENSION,
    //     jDoodleAPITemplateConfiguration: {
    //         language: "java",
    //         version: "4",
    //         compileOnly: false
    //     }
    // }

};