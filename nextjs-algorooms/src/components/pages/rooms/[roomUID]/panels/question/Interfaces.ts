export interface questionExampleInterface {
    questionExampleInput: string;
    questionExampleOutput: string;
    questionExampleExplanation: string;
};

export interface questionPanelInterface {
    questionIndex: number;
    questionTitle: string;
    questionDifficulty: string;
    questionBody: string;
    questionExamples: questionExampleInterface[];
    questionConstraints: string[];
    questionHints: string[];
    questionTopics: string[];
};