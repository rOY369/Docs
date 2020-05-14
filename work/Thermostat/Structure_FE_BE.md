## Overview

The following document states the fundamental requirements and structure of thermostat from a technical point of view especially to assist frontend and backend team.

The basic working of thermostat is as follows : 

- The core of thermostat is `PID controller` which observes a parameter namely `temperature` and calculates output namely `vfd - outputfrequency` or `actuator - valve open %` based on how far is `temperature` from `setpoint`.
- Thermostat also involves some *additional logic* which is targeted either towards energy saving, thermal comfort and handling any critical situation. 
- Additional logic 1 : thermostat returns `minimum position` output for a controllable if `ahu status` is off.
- Additional logic 2 : If thermostat is unable to observe any parameter, it returns `emergency position` output to a controllable.
- Thermostat operates in cycles of modulation. A modulation cycle starts when there is cooling demand. It detects this cooling demand from `temperature` observation in relation to `setpoint` and `offset`. If there is no cooling demand, it returns `minimum position` as output.
- Modulation cycle ends when `setpoint` is met. 

**Thermostat is similar to recipe** in the following ways :

- Thermostat takes some observations as input and returns output.
- There is a specific frequency of when should thermostat should observe and take action. This is precisely the `sample time`. This is implemented by  using a cron expression. 
- Thermostat can be scheduled.

**Thermostat is different from recipe** in the way that the evaluation is not simple and involves some steps. In recipe the evaluation is `observation` --> `if condition is true` --> `take action`. In thermostat, the evaluation is `observation` --> `thermostat logic` --> `take action`.  The `thermostat logic` is itself a series of custom logic designed exclusively to tackle the problem of energy and thermal comfort optimisation.

**Thermostat is a type of recipe.**

## Characteristics of a thermostat recipe

-  It is somehow mapped to an `AHU` as `ahu status` is required as an observation parameter. 
- A thermostat recipe will control only one device precisely any of `actuator` or `vfd`. 
- A thermostat recipe is entirely different, runs entirely independent and isolated from any other thermostat recipe even if both are mapped to the same `AHU`. 
- It involves some extra configuration parameters apart from the basic configuration structure of a normal recipe.


## Recipe Configuration

	- Observation details (`dataExpression`)
		- `ahu status` :
			- `status` expression from component configuration page
			- Example - `1155.kva > 0.3` 
		- `temperature` : expression entered by user. Can involve any devices giving temperature data.
		- Topics : 
			- `["db/2101/tmp/2","db/1155/kva/2"]`
			- The number of observation points i.e. `2` in the above example is fixed for thermostat.
	- Command details
		- Destination : 
			- Controllable `deviceId` and `parameter`.
			- Example of `vfd` as controllable : `3123` , `setfrequency`
			- Example of `actuator` as controllable : `1192`, `changesetpoint`
- Thermostat specific settings
	- General :
		- `setpoint`  in degC
		- `minimum offset` in degC
		- `maximum offset` in degC
		- `time to achieve setpoint` in minutes
		- `app mode` - cooling or heating
	- Controllable settings :
		- `type` - can be `actuator` or `vfd`
		- `modulation range` in the form of `(__%) - (__%)`. Example 80% - 90%.
		- `minimum position` in % 
		- `emergency position` in %
		- `sampleTime` in minutes. 
		- `modulation speed` - can be any number from 1 to 5.

The above parameters fall in the recipe config as shown in the following structure. This structure belongs to a thermostat recipe in the recipe table of IoT database.

```
{
  "maxDataNeeded": 0,
  "everyMinuteTopics": [
    "db/2132/tmp/2",
    "db/2175/feedback/2"
  ],
  "startNow": "True",
  "alwaysRun": "false",
  "actionAlert": [
    {
      "command": "changesetpoint",
      "did": "2172",
      "parent": "mgch_9",
      "value": "evaluate",
      "title": "thermal_app",
      "type": "action",
      "notify": [],
      "accountable": [],
      "priority": 1,
      "uniqId": ""
    }
  ],
  "syncAsyncAction": "True",
  "failsafe": "{}",
  "dependentOnOthers": "[]",
  "runOn": "2757",
  "notRun": "[]",
  "switchOff": 0,
  "controllers": "[]",
  "maxLogsNeeded": 0,
  "topics": [
    "db/2132/tmp/2",
    "db/2175/feedback/2"
  ],
  "rid": "1677674e-4d65-11ea-a034-40a5efd61c84",
  "appType": "thermal",
  "misc": {
    "appSettings": {
      "setpoint": 25,
      "minOffset": 0.2,
      "maxOffset": 0.5,
      "timeToAchieve": 20,
      "appMode": "cooling"
    },
    "controlSettings": {
      "name": "actuator",
      "emergencyPosition": 80,
      "minimumPosition": 20,
      "minModulation": 60,
      "maxModulation": 97,
      "modulationSpeed": 2,
      "sampleTime": 5
    },
    "dataExpression": {
      "temp": "2132.tmp",
      "ahuStatus": "2175.kva > 0.3"
    }
  }
}
```

The keys with fixed values in the above structure are as follows : 
- `"maxDataNeeded"`
- `"startNow": "True"`
- `"alwaysRun": "false"`
-  `"actionAlert": [
    {
      "value": "evaluate",
      "title": "thermal_app",
      "type": "action",
      "notify": [],
      "accountable": [],
      "priority": 1,
    }
  ]`
  - `"syncAsyncAction": "True"`
  - `"failsafe": "{}"`
  - `"dependentOnOthers": "[]"`
  - `"notRun": "[]"`
  - `"switchOff": 0`
  - `"controllers": "[]"`
  - `"maxLogsNeeded": 0`
  - `"appType": "thermal"`

## Schedule Configuration

The schedule of a recipe is nothing but a cron expression. This cron expression will depend on the `sample time` parameter in `control settings` and other scheduling features which already exist.

## Modes

There will be 3 modes which a user can select - `jouletrack`, `joulerecipe` or `pid`. The modes can be considered as sources. At a given point of time, only command from the configured source/mode will be allowed to execute.

## Dynamic Setpoint

- **Scheduling thermostat with different setpoint** -  Suppose there is a thermostat recipe configured with `setpoint = 25`. The user has configured all parameters successfully and thermostat starts modulating the controllable. It is also a requirement from the thermostat software that the user can conveniently configure the same recipe with a different `setpoint` and deploy it with a different schedule. 
- **Thermostat recipe triggered by an observation** -  
<!--stackedit_data:
eyJoaXN0b3J5IjpbODkzOTE2MjI2XX0=
-->