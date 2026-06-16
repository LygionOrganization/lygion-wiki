# LinkArm-LT Integration and Dimensions

Power the arm from DC 9-12.6 V with enough current for all simultaneous joint loads. USB is for controller power, communication, and development; it is not the recommended actuator supply.

Use the mounting-hole drawing or the supplied DXF/PDF files when designing a mobile base or fixture:

- [Extended dimensions PDF](../../../../reference/robots/linkarm-lt/assets/LinkArm_LT.pdf)
- [Folded dimensions PDF](../../../../reference/robots/linkarm-lt/assets/LinkArm_LT_folded.pdf)
- [2D CAD drawing DXF](../../../../reference/robots/linkarm-lt/assets/LinkArm_LT_dxf.dxf)

!!! warning "Verify the physical revision before machining"
    Production revisions can differ. Measure the actual arm and confirm the drawing version before drilling or batch manufacturing.

Allow space for the full workspace, cable bend radius, gripper payload, emergency access, and center-of-gravity changes. Host integration can use USB CDC, HTTP, or WebSocket.

