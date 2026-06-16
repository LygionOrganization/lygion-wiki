# ESP-NOW Synchronized Teaching

ESP-NOW can make one LinkArm-LT act as a leader while one or more follower arms reproduce its commands.

!!! danger "Followers may move suddenly"
    Secure every arm, clear every workspace, and test at low speed before enabling synchronization.

Configure the leader and followers through the web console or JSON interface. Broadcast mode is convenient for demonstrations; a known-MAC peer list is better when only specific robots should follow.

Define a safe startup mode and a communication-timeout behavior. To exit synchronized teaching, disable the follower mode and restart or reinitialize control as required by the current firmware.

