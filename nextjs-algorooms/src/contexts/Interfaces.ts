export interface roomContextLayerInterface {
    uid: string,
    members: any[],
    setMembers?: Function,
    messages: any[],
    setMessages?: Function,
    language: string,
    setLanguage?: Function,
    code: string,
    setCode?: Function,
    socket: any
};