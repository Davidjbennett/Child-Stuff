var groups = [];
$(".column :radio").each(function () { // Make entry for each input field.
    if (groups.indexOf(this.name) < 0) {
        groups.push(this.name);
    }
});

$(":radio").change(function () {
    var checked = $(".column :radio:checked"); // Counts the no. of checked radio buttons.
    if (groups.length == checked.length) { // This means that all the radio buttons are checked.
        // If all the radio buttons are checked we make another function call that evaluates the score.
        updateScore();
    }
});

function updateScore() {
    /*
    ScoreFinal = (ScopeStatus) ∗ ( (3.326258289∗ScoreBase) + (1.1∗ScoreExploitability) )
    
    ScopeStatus =>
    Unchanged = 1.0
    Changed = 1.08
    
    */
    // So we have 3 parts to solve we will solve each part one by one.
    // First of all let's start with ScopeStatus.
    var check = $("input[name='scope']:checked").val();
    var ScopeStatus = 0;

    if (check == 'scope_U') { // Check if the scope is unchanged.
        ScopeStatus = 1.0;
    }
    else if (check == 'scope_C') { // Checks if it is changed.
        ScopeStatus = 1.08;
    }

    /*
    Now we will find the ScoreBase.
    ScoreBase = BaseConfidentiality + BaseIntegrity + BaseAvailability
    
    BaseConfidentiality =>
    Sensitivity / Confidentiality None Low High
    None 0.00 0.22 0.56
    Low 0.00 0.65 0.75
    High 0.00 0.85 0.95
    
    BaseIntegrity =>
    Health Impact / Integrity None Low High
    None 0.00 0.22 0.56
    Low 0.55 0.60 0.75
    High 0.85 0.90 0.95
    
    Base Availability =>
    Health Impact / Availability None Low High
    None 0.00 0.22 0.56
    Low 0.55 0.60 0.65
    High 0.85 0.90 0.95
    
    */

    // First of finding the values of all the radio buttons.
    var sens = $("input[name='sens']:checked").val(); // Sensitivity
    var conf = $("input[name='conf']:checked").val(); // Confidentiality
    var health = $("input[name='health']:checked").val(); // Health Impact
    var integ = $("input[name='integ']:checked").val(); // Integrity
    var avail = $("input[name='avail']:checked").val(); // Availability

    // Now we have all the values we just to map the appropriate values.
    // Here also we will find values one by one.
    // BaseConfidentiality
    var BaseConfidentiality;
    if (sens == 'sens_N') {
        if (conf == 'conf_N') {
            BaseConfidentiality = 0.00;
        }
        else if (conf == 'conf_L') {
            BaseConfidentiality = 0.22;
        }
        else if (conf == 'conf_H') {
            BaseConfidentiality = 0.56;
        }
    }
    else if (sens == 'sens_L') {
        if (conf == 'conf_N') {
            BaseConfidentiality = 0.00;
        }
        else if (conf == 'conf_L') {
            BaseConfidentiality = 0.65;
        }
        else if (conf == 'conf_H') {
            BaseConfidentiality = 0.75;
        }
    }
    else if (sens == 'sens_H') {
        if (conf == 'conf_N') {
            BaseConfidentiality = 0.00;
        }
        else if (conf == 'conf_L') {
            BaseConfidentiality = 0.85;
        }
        else if (conf == 'conf_H') {
            BaseConfidentiality = 0.95;
        }
    }


    // BaseIntegrity
    var BaseIntegrity;
    if (health == 'health_N') {
        if (integ == 'integ_N') {
            BaseIntegrity = 0.00;
        }
        else if (integ == 'integ_L') {
            BaseIntegrity = 0.22;
        }
        else if (integ == 'integ_H') {
            BaseIntegrity = 0.56;
        }
    }
    else if (health == 'health_L') {
        if (integ == 'integ_N') {
            BaseIntegrity = 0.55;
        }
        else if (integ == 'integ_L') {
            BaseIntegrity = 0.60;
        }
        else if (integ == 'integ_H') {
            BaseIntegrity = 0.75;
        }
    }
    else if (health == 'health_H') {
        if (integ == 'integ_N') {
            BaseIntegrity = 0.85;
        }
        else if (integ == 'integ_L') {
            BaseIntegrity = 0.90;
        }
        else if (integ == 'integ_H') {
            BaseIntegrity = 0.95;
        }
    }

    // BaseAvailability
    var BaseAvailability;
    if (health == 'health_N') {
        if (avail == 'avail_N') {
            BaseAvailability = 0.00;
        }
        else if (avail == 'avail_L') {
            BaseAvailability = 0.22;
        }
        else if (avail == 'avail_H') {
            BaseAvailability = 0.56;
        }
    }
    else if (health == 'health_L') {
        if (avail == 'avail_N') {
            BaseAvailability = 0.55;
        }
        else if (avail == 'avail_L') {
            BaseAvailability = 0.60;
        }
        else if (avail == 'avail_H') {
            BaseAvailability = 0.65;
        }
    }
    else if (health == 'health_H') {
        if (avail == 'avail_N') {
            BaseAvailability = 0.85;
        }
        else if (avail == 'avail_L') {
            BaseAvailability = 0.90;
        }
        else if (avail == 'avail_H') {
            BaseAvailability = 0.95;
        }
    }

    var ScoreBase = BaseConfidentiality + BaseIntegrity + BaseAvailability; // The second variable for our final score evaluated.
    // console.log(ScoreBase)
    /*
    ScoreExploitability = AttackVector * AttackComplexity * PrivilegedRequired * UserInteraction
    
    AttackVector(Selection)=
    Attack Vector Value
    Network 0.85
    Adjacent Network 0.62
    Local 0.55
    Physical 0.20
    
    AttackComplexity(Selection)=
    Attack Complexity Value
    Low 0.77
    High 0.44
    
    PrivilegeRequired(Selection)=
    Privilege Required Value
    None 0.85
    Low 0.62
    High 0.27
    
    UserInteraction(Selection)=
    User Interaction Value
    None 0.85
    Required 0.62
    */

    // Finding the selected radios first.
    var av = $("input[name='AV']:checked").val(); // Attack Vector
    var ac = $("input[name='AC']:checked").val(); // Attack Complexity
    var priv = $("input[name='PR']:checked").val(); // Privileges Required
    var ui = $("input[name='UI']:checked").val(); // User Interaction
    var AttackVector;
    var AttackComplexity;
    var PrivilegedRequired;
    var UserInteraction;

    if (av == 'AV_N') { // Evaluating Attack Vector
        AttackVector = 0.85;
    }
    else if (av == 'AV_A') {
        AttackVector = 0.62;
    }
    else if (av == 'AV_L') {
        AttackVector = 0.55;
    }
    else if (av == 'AV_P') {
        AttackVector = 0.20;
    }

    if (ac == 'AC_L') { // Evaluating Attack Complexity
        AttackComplexity = 0.77;
    }
    else if (ac == 'AC_H') {
        AttackComplexity = 0.44;
    }

    if (priv == 'PR_N') { // Evaluating Privilege Required
        PrivilegedRequired = 0.85;
    }
    else if (priv == 'PR_L') {
        PrivilegedRequired = 0.62;
    }
    else if (priv == 'PR_H') {
        PrivilegedRequired = 0.27;
    }

    if (ui == 'UI_N') { // Evaluating User Interface
        UserInteraction = 0.85;
    }
    else if (ui == 'UI_R') {
        UserInteraction = 0.62;
    }

    var ScoreExploitability = AttackVector * AttackComplexity * PrivilegedRequired * UserInteraction;

    // Now we have evaluated all the values that we need to find the final score.

    var ScoreFinal;
    ScoreFinal = ScopeStatus.toFixed(2) * ((3.326258289 * ScoreBase.toFixed(2)) + (1.1 * ScoreExploitability.toFixed(2)));
    ScoreFinal = (Math.ceil(ScoreFinal.toFixed(1) * 10.0) / 10.0);
    ScoreFinal += .05

    if (ScoreBase == 0){ScoreFinal = 0.0}
    if (ScoreBase >= 10){ScoreBase = 10.0}

    document.getElementById('score').innerHTML = ScoreFinal.toFixed(1);
    document.getElementById('warning').style.display = 'none';
}