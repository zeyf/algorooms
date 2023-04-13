export interface roomMemberInterface {
    member: string;
    backgroundColor: string
};

export interface roomMembersInterface {
    members: memberInterface[];
};

export interface roomSettingsInterface {
    topics: string[];
    difficulty: string;
    link: string;
};

export interface roomSettingsModalInterface {
    topics: string[];
    difficulty: string;
    link: string;
};

export interface memberInterface {
  name: string;
  color: string;
}