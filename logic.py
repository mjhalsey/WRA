import json

class LegalReadinessQuiz:
    """
    This class contains the logic and data for the full Legal Readiness Questionnaire.
    It manages the flow of questions, tracks the user's results, and provides the
    final checklist.
    """
    def __init__(self):
        # This dictionary holds the entire questionnaire logic.
        # It is organized into 9 distinct sections.
        self.nodes = {
                        "start": {
                "type": "section_intro",
                "text": "Welcome to the Warfighter Legal Readiness Program. We are here to help you understand your legal needs and connect you with a lawyer who can help. This process is simple and fast, and will give you peace of mind as you prepare for deployment. The questions and information provided have been drafted by Legal Assistance experts with years of experience helping Warfighters prepare for deployments.\n\nAnswering the questions below can help us understand what you are going through and whether you need legal assistance. These answers are not a substitute for legal advice, but they will give you an idea if you should contact an attorney. When you complete all the questions, the program will generate a checklist and instructions based on your responses. You can take that checklist to your local legal assistance office and the lawyers there will help you put together what you need, at no cost to you.\n\nPlease read each question carefully.\n\nLet’s get started……..",
                "next": "wills_intro"
            },


            # =================================================================
            # SECTION 1: WILLS AND ESTATE PLANNING
            # =================================================================
            
                                        "wills_intro": {
            "type": "section_intro",
            "title": "Section 1: Wills and Estate Planning",
            "text": "Estate planning is the process of deciding exactly what you want to happen to your money, stuff, and even your children if you pass away or become unable to make decisions for yourself. It's not just for the wealthy; everyone has an \"estate.\" Estate planning answers these big questions: Who gets my stuff? (Your house, car, money, sentimental items). Who will take care of my kids? (Designating a guardian). Who will make medical decisions for me if I can't? (Healthcare power of attorney). The goal of estate planning is to make things as easy as possible for your Family during a difficult time, and an important part of an estate plan can be a will.",
            "popup": {"A Will": "A Will is the document that decides what you want to happen to your stuff. Think of it as the master instruction sheet for what to do with your things after you pass away. A Will does three main things: 1. It lists who gets your stuff. 2. It names a trusted person (sometime called your \"Executor\" or your “Personal Representative”) to be in charge of making sure your will is followed. 3. It names a Guardian if you have minor children - this is where you legally state who you want to raise them. Remember, no one can force you to get a will, and you are not required to have one before you deploy. These questions will tell you when it’s a really really good idea to make a will, but the choice is always yours. Later in the program we will talk about how to make sure all your benefits and accounts can be directed to where you want them to go with or without a will."},
            "next": "q_married"
        },


            "q_married": {
                "type": "question",
                "text": "Are you married?",
                "yes": "q_separated",
                "no": "q_single_have_children"
            },
            # --- Married Path ---
                    "q_separated": {
            "type": "question",
            "text": "Are you currently separated, going through legal separation, or divorce?",
            "yes": "out_wills_separated",
            "no": "q_married_have_children"
        },
        "out_wills_separated": {
            "type": "outcome",
            "level": "Red",
            "text": "You should see an attorney to help you get a will. If you don’t get a will, there is a chance your soon-to-be-ex-spouse will inherit your stuff or be able to make important decisions on your behalf.",
            "next": "q_married_have_children" # <--- THE FIX. This now correctly asks about children.
        },

            "q_married_have_children": {
                "type": "question",
                "text": "Do you have children?",
                "yes": "q_custody_dispute_married",
                "no": "out_wills_married_no_children"
            },
            "out_wills_married_no_children": {
                "type": "outcome",
                "level": "Yellow",
                "text": "If you die without a will, your stuff will go to your spouse. If you don’t want that to happen, you should consider seeing an attorney.",
                "next": "asset_intro" # Jumps to the next section
            },
            "q_custody_dispute_married": {
                "type": "question",
                "text": "Do you have any children whose custody or support is currently in dispute?",
                "yes": "out_wills_custody_dispute",
                "no": "q_children_special_needs"
            },
            "out_wills_custody_dispute": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You should consider seeing an attorney to talk about how to proceed with your family law matter while deployed.",
                "next": "q_children_special_needs"
            },
            "q_children_special_needs": {
                "type": "question",
                "text": "Do your children have special needs or need a legal guardian?",
                "yes": "out_wills_guardian",
                "no": "q_all_children_are_spouses"
            },
            "out_wills_guardian": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to help you get a will. Your will can appoint a guardian to take care of your children.",
                "next": "q_all_children_are_spouses"
            },
            "q_all_children_are_spouses": {
                "type": "question",
                "text": "Are all of your children the biological or legally adopted children of your spouse?",
                "yes": "q_spouse_deploying",
                "no": "out_wills_step_children"
            },
            "out_wills_step_children": {
                "type": "outcome",
                "level": "Yellow",
                "text": "States have different rules about what happens when someone dies without a will (the formal term is ‘intestate’). Depending on where you live, your state will have rules about how stepparents, children from outside of the current marriage, and/or biological children have a right to your stuff. You should consider seeing an attorney to talk about drafting a will if you don’t like what your state laws say about where your stuff will go.",
                "popup": {"intestate": "intestate means dying without a will. Every state has a set of intestacy laws that determine who gets your stuff if you die without a will."},
                "next": "asset_intro"
            },
            "q_spouse_deploying": {
                "type": "question",
                "text": "Is your spouse also deploying at this time?",
                "yes": "out_wills_spouse_deploys",
                "no": "out_wills_intestate_spouse"
            },
            "out_wills_spouse_deploys": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to help you draft a will and talk about custody, if necessary.",
                "next": "asset_intro"
            },
            "out_wills_intestate_spouse": {
                "type": "outcome",
                "level": "Yellow",
                "text": "If you die without a will, your stuff will go to your spouse or be split between your spouse and children (depending on where you live). Dying without a will is called “intestate”. You should consider seeing an attorney to talk about getting a will if you don’t want that to happen.",
                "popup": {"intestate": "intestate means dying without a will. Every state has a set of intestacy laws that determine who gets your stuff if you die without a will"},
                "next": "asset_intro"
            },
            # --- Single Path ---
            "q_single_have_children": {
                "type": "question",
                "text": "Do you have children?",
                "yes": "q_single_fcp_complete",
                "no": "q_single_parents_alive"
            },
            "q_single_fcp_complete": {
                "type": "question",
                "text": "Do you have a Family Care Plan and is it complete and certified by your unit?",
                "yes": "q_single_custody_dispute",
                "no": "out_wills_fcp"
            },
            "out_wills_fcp": {
                "type": "outcome",
                "level": "Red",
                "text": "You should create a Family Care Plan.",
                "next": "q_single_custody_dispute"
            },
            "q_single_custody_dispute": {
                "type": "question",
                "text": "Do you have any children whose custody or support is currently in dispute?",
                "yes": "out_wills_family_law_issues",
                "no": "q_single_ever_married"
            },
            "out_wills_family_law_issues": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to resolve any family law issues.",
                "next": "q_single_ever_married"
            },
            "q_single_ever_married": {
                "type": "question",
                "text": "Have you ever been married to the person you had children with?",
                "yes": "out_wills_review_old",
                "no": "q_single_children_minors"
            },
            "out_wills_review_old": {
                "type": "outcome",
                "level": "Red",
                "text": "Since you were previously married, now is an important time to check any previous wills to make sure you have all the right people in the will or out of the will. You should see an attorney to review any old wills to help you change it, or draft a new one.",
                "next": "q_single_children_minors"
            },
            "q_single_children_minors": {
                "type": "question",
                "text": "Are your children minors or adults with special needs who require a guardian?",
                "popup": {"guardianship": "a guardianship is a legal designation that a court has approved someone to take care of a minor child or someone who is incapable of caring for themselves. A guardianship gives that person important legal rights such as the ability to seek medical care for the child or enroll them in school"},
                "yes": "out_wills_estate_planning_single",
                "no": "q_single_disinherit"
            },
            "out_wills_estate_planning_single": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to complete estate planning documentation.",
                "next": "q_single_disinherit"
            },
            "q_single_disinherit": {
                "type": "question",
                "text": "If you die without a will, your estate will be distributed to your children. Do you want to disinherit one or more of your children?",
                "yes": "out_wills_disinherit_yes",
                "no": "out_wills_disinherit_no"
            },
            "out_wills_disinherit_yes": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to complete estate planning documentation.",
                "next": "asset_intro"
            },
            "out_wills_disinherit_no": {
                "type": "outcome",
                "level": "Green",
                "text": "Continue to next question.",
                "next": "asset_intro"
            },
            "q_single_parents_alive": {
                "type": "question",
                "text": "Are your parents alive? If you die without a will, your property will go to them.",
                "yes": "out_wills_happy_with_parents",
                "no": "q_single_siblings"
            },
            "out_wills_happy_with_parents": {
                "type": "outcome",
                "level": "Yellow",
                "text": "If you are happy with your property going to your parents, you do not need a will. If not, you should see an attorney to draft a will.",
                "next": "asset_intro"
            },
            "q_single_siblings": {
                "type": "question",
                "text": "Do you have siblings? If you die without a will, your property will go to them.",
                "yes": "out_wills_happy_with_siblings",
                "no": "out_wills_single_no_heirs"
            },
            "out_wills_happy_with_siblings": {
                "type": "outcome",
                "level": "Yellow",
                "text": "If you are happy with your property going to your siblings, you do not need a will. If not, see an attorney.",
                "next": "asset_intro"
            },
            "out_wills_single_no_heirs": {
                "type": "outcome",
                "level": "Red",
                "text": "If you die without a will, your property will go to the state. You should see an attorney to draft a will to ensure your property goes where you want it to.",
                "next": "asset_intro"
            },
                "asset_intro": {
            "type": "section_intro",
            "title": "Section 2: Asset Check",
            "text": "Congrats – you just made it through one of the most important and difficult topics to think about before a deployment. Putting in the work now will give you and your family peace of mind. Do you also know that if you had paid a private attorney for this service it probably would have cost you thousands of dollars? Free legal advice is a benefit of military service that you have earned – good job taking advantage of this valuable benefit.",
            "next": "q_own_land"
        },


            
            # =================================================================
            # SECTION 2: ASSET CHECK
            # =================================================================
            
                        
            "q_own_land": {
                "type": "question",
                "text": "Do you own a house or land?",
                "yes": "out_asset_estate_planning_1",
                "no": "q_specific_gifts"
            },
            "out_asset_estate_planning_1": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to complete estate planning documentation.",
                "next": "q_specific_gifts" # This was a bug in the flowchart, should go to next question not end
            },
            "q_specific_gifts": {
                "type": "question",
                "text": "Do you have specific things you want to give to a friend or a charity?",
                "yes": "out_asset_estate_planning_2",
                "no": "q_over_1m"
            },
            "out_asset_estate_planning_2": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to complete estate planning documentation.",
                "next": "q_over_1m" # This was a bug in the flowchart, should go to next question not end
            },
            "q_over_1m": {
                "type": "question",
                "text": "Do you have more than $1,000,000 worth of money and property?",
                "yes": "out_asset_complex_1",
                "no": "q_farm_business"
            },
            "out_asset_complex_1": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You should consider seeing an attorney to talk about getting a will. They may have to refer you to a civilian attorney as there may be different plans you can create to save your family time or money if you die.",
                "next": "q_farm_business"
            },
            "q_farm_business": {
                "type": "question",
                "text": "Do you own a farm or business?",
                "yes": "out_asset_complex_2",
                "no": "q_in_trust"
            },
            "out_asset_complex_2": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You should consider seeing an attorney to talk about getting a will. They may have to refer you to a civilian attorney as your estate may be too complex.",
                "next": "q_in_trust"
            },
            "q_in_trust": {
                "type": "question",
                "text": "Is your money or property held in a trust?",
                "yes": "out_asset_complex_3",
                "no": "out_asset_pod"
            },
            "out_asset_complex_3": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You should consider seeing an attorney to talk about getting a will. They may have to refer you to a civilian attorney as your estate may be too complex.",
                "next": "out_asset_pod"
            },
            "out_asset_pod": {
                "type": "outcome",
                "level": "Green",
                "text": "You should update your 'Payable on Death' beneficiaries with your bank.",
                "next": "beneficiary_intro" # Correctly points to the next section
            },

            # =================================================================
            # SECTION 3: BENEFICIARY DESIGNATIONS
            # =================================================================

                                "beneficiary_intro": {
            "type": "section_intro",
            "title": "Section 3: Beneficiary Designations",
            "text": "That's excellent work. You've taken a crucial step by assessing what you have. Now that you have a clear picture of your assets, the next logical step is to ensure those assets—and your military benefits—are directed to the right people. Let's look at your beneficiary designations.",
            "popup": {"Beneficiary": "A beneficiary is a person or entity you name in a will, life insurance policy, or other financial account who will receive money or property from you when you pass away."},
            "next": "q_sgli_updated"
        },

            "q_sgli_updated": {
                "type": "question",
                "text": "Have you checked your SGLI (Servicemembers' Group Life Insurance) beneficiary designations and are they up to date?",
                "yes": "q_sgli_divorced",
                "no": "out_bene_update_sgli"
            },
            "out_bene_update_sgli": {
                "type": "outcome",
                "level": "Red",
                "text": "You should update your SGLI immediately.",
                "next": "q_sgli_divorced" # Still need to ask the divorce question
            },
            "q_sgli_divorced": {
                "type": "question",
                "text": "Are you divorced? If so, have you taken your former spouse off your SGLI?",
                "yes": "out_bene_remove_ex_spouse", # This implies they are divorced but haven't removed the ex.
                "no": "q_dd93_updated", # This implies they are either not divorced, or have already handled it.
            },
            "out_bene_remove_ex_spouse": {
                 "type": "outcome",
                 "level": "Red",
                 "text": "You should check your SGLI immediately and update your beneficiary.",
                 "next": "q_dd93_updated"
            },
            "q_dd93_updated": {
                "type": "question",
                "text": "Have you checked your Record of Emergency Data (DD Form 93) and is it up to date?",
                "popup": {"DD Form 93": "Your DD93 is one of the most important documents you will have as a service member. This document tells the Army who you want to receive certain benefits, such as the death gratuity (currently $100,000, tax free) and your final pay and allowances. You can update this form at any time and it is a good idea to check it before every deployment."},
                "yes": "q_tsp_updated",
                "no": "out_bene_dd93"
            },
            "out_bene_dd93": {
                "type": "outcome",
                "level": "Red",
                "text": "You should update your Record of Emergency Data (DD Form 93) immediately.",
                "next": "q_tsp_updated"
            },

            "q_tsp_updated": {
                "type": "question",
                "text": "Have you checked your TSP and other retirement account beneficiaries and are they up to date?",
                "yes": "reemployment_intro", # Points to the next section
                "no": "out_bene_update_retirement"
            },
            "out_bene_update_retirement": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You may want to consider checking your TSP and other retirement accounts to make sure your beneficiaries are up to date.",
                "next": "reemployment_intro" # Points to the next section
            },

            


            # =================================================================
            # SECTION 4: REEMPLOYMENT RIGHTS (USERRA)
            # =================================================================

                                "reemployment_intro": {
            "type": "section_intro",
            "title": "Section 4: Reemployment Rights (USERRA)",
            "text": "It’s important to understand that a will doesn’t cover everything you own. There are a lot of valuable assets that are controlled very simply – by just writing down who you want to receive the benefit in a beneficiary designation. Most of these types of assets are in monetary accounts like bank accounts, retirement accounts like IRAs or 401ks, insurance policies, or investment accounts. Almost every institution that offers these type accounts give you an easy way to change these designations – they may be called a “pay on death” (POD) designation, or a beneficiary designation, or a successor designation. Working through this section helped you identify and take care of many of these important accounts.",
            "popup": {"USERRA": "The Uniformed Services Employment and Reemployment Rights Act (USERRA) is a federal law that protects the civilian job rights and benefits for veterans and members of reserve components. It requires employers to allow you to return to your job after military service."},
            "next": "q_has_civilian_job"
        },

            "q_has_civilian_job": {
                "type": "question",
                "text": "Do you have a civilian job that you will be leaving for your deployment?",
                "yes": "q_notified_employer",
                "no": "scra_intro" # If no job, skip to the next section
            },
            "q_notified_employer": {
                "type": "question",
                "text": "Have you notified your employer of your upcoming deployment?",
                "yes": "scra_intro", # If yes, continue to the next section
                "no": "out_reemployment_notify"
            },
            "out_reemployment_notify": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You should notify your employer of your military service to protect your re-employment rights under USERRA.",
                "next": "scra_intro" # Continue to the next section
            },


            # =================================================================
            # SECTION 5: CONSUMER PROTECTION (SCRA)
            # =================================================================

                                "scra_intro": {
            "type": "section_intro",
            "title": "Section 5: Consumer Protection and the Servicemember's Civil Relief Act (SCRA)",
            "text": "That's great. Taking a moment to think about your civilian employment is a crucial step. Federal law gives you powerful rights to get your job back, and the step you just took—or confirmed you already took—is key to ensuring you're protected.\n\nNow, let's move on to another powerful set of federal protections: your rights as a consumer under the SCRA.",
            "popup": {"SCRA": "The Servicemembers Civil Relief Act (SCRA) is a federal law that provides a range of legal protections to active-duty servicemembers. It can help with things like breaking a lease, reducing interest rates, and postponing court actions."},
            "next": "q_landlord_tenant"
        },

            "q_landlord_tenant": {
                "type": "question",
                "text": "Do you have any landlord/tenant issues, or are you currently in a lease you may need to break?",
                "yes": "out_consumer_lease",
                "no": "q_debt_issues"
            },
            "out_consumer_lease": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You should consider seeing an attorney to learn about your rights under the SCRA.",
                "next": "q_debt_issues"
            },
            "q_debt_issues": {
                "type": "question",
                "text": "Do you have any significant debt issues or are you having trouble with debt collectors?",
                "yes": "out_consumer_debt",
                "no": "q_court_date"
            },
            "out_consumer_debt": {
                "type": "outcome",
                "level": "Yellow",
                "text": "You should consider seeing an attorney to learn about your rights under the SCRA.",
                "next": "q_court_date"
            },
            "q_court_date": {
                "type": "question",
                "text": "Do you have any upcoming court dates or other civil legal matters pending?",
                "yes": "out_consumer_court",
                "no": "admin_intro" # Points to the next section
            },
            "out_consumer_court": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney immediately to discuss how to handle your pending legal matters while you are deployed.",
                "next": "admin_intro" # Points to the next section
            },


            # =================================================================
            # SECTION 6: MILITARY ADMINISTRATIVE MATTERS
            # =================================================================

                                        "admin_intro": {
            "type": "section_intro",
            "title": "Section 6: Military Administrative Matters",
            "text": "Excellent work. By navigating these questions, you have taken proactive steps to safeguard your financial life while you are deployed. This is a critical part of readiness.\n\nRemember, if you flagged any issues in this section, your personalized checklist will give you clear next steps, including helpful resources for contacting your creditors.\n\nNow, let's move on to a few quick administrative items.",
            "next": "q_fcp_check_admin"
        },

        "q_fcp_check_admin": {
            "type": "question",
            "text": "Do you have a Family Care Plan, and is it complete and certified by your unit?",
            "yes": "immigration_intro", # Points to the next section
            "no": "out_admin_fcp"
        },
        "out_admin_fcp": {
            "type": "outcome",
            "level": "Red",
            "text": "You should create a Family Care Plan.",
            "next": "immigration_intro" # Points to the next section
        },



            # =================================================================
            # SECTION 7: IMMIGRATION
            # =================================================================

                        "immigration_intro": {
                "type": "section_intro",
                "title": "Section 7: Immigration",
                "text": "One last push!",
                "next": "q_is_citizen"
            },
            "q_is_citizen": {
                "type": "question",
                "text": "Are you a U.S. Citizen?",
                "yes": "q_relative_needs_benefit",
                "no": "out_immigration_not_citizen"
            },
            "out_immigration_not_citizen": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to discuss how you can become a U.S. Citizen. There are special laws that may make it easier for you.",
                "next": "q_relative_needs_benefit"
            },
            "q_relative_needs_benefit": {
                "type": "question",
                "text": "Do you have an immediate relative (spouse, child, or parent) who needs an immigration benefit?",
                "yes": "out_immigration_relative_benefit",
                "no": "poa_intro" # Points to the next section
            },
            "out_immigration_relative_benefit": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to discuss whether your relative qualifies for any immigration benefits, such as parole in place.",
                "next": "poa_intro" # Points to the next section
            },


            # =================================================================
            # SECTION 8: POWERS OF ATTORNEY
            # =================================================================

                        "poa_intro": {
                "type": "section_intro",
                "title": "Section 8: Powers of Attorney",
                "text": "You're in the home stretch! This last section covers important legal tools and protections.",
                "popup": {"Power of Attorney": "A Power of Attorney (POA) is a legal document that allows you to appoint someone to make financial or legal decisions on your behalf while you are gone or unable to do so."},
                "next": "q_medical_wishes"
            },
            "q_medical_wishes": {
                "type": "question",
                "text": "Do you have a plan for your medical wishes if you get very sick or if you are unable to make decisions for yourself?",
                "yes": "q_poa_needed",
                "no": "out_poa_medical_directive"
            },
            "out_poa_medical_directive": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to talk about whether you need a living will, a healthcare directive, and/or an advanced medical directive.",
                "popup": {"healthcare directive": "A healthcare directive, also known as a living will or advance directive, is a legal document that outlines your wishes for medical care in the event you are unable to communicate them yourself. It allows you to appoint a person, often called a healthcare agent or proxy, to make medical decisions on your behalf."},
                "next": "q_poa_needed"
            },
            "q_poa_needed": {
                "type": "question",
                "text": "Do you need someone to pay bills, manage your bank accounts, or handle other financial matters while you are deployed?",
                "yes": "q_has_poa",
                "no": "final_question_intro" # Points to the next section
            },
            "q_has_poa": {
                "type": "question",
                "text": "Do you already have a Power of Attorney?",
                "yes": "final_question_intro", # Points to the next section
                "no": "out_poa_get_one"
            },
            "out_poa_get_one": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see an attorney to get a Power of Attorney.",
                "next": "final_question_intro" # Points to the next section
            },


            # =================================================================
            # SECTION 9: FINAL QUESTION
            # =================================================================

                                "final_question_intro": {
            "type": "section_intro",
            "title": "Section 9: Final Question",
            "text": "You've reached the final step! You have now covered all the major legal readiness topics, from estate planning to consumer law.\n\nThis last question is our safety net, designed to catch any unique concerns that weren't covered in the previous sections. Please take a moment to think if there is anything else on your mind.\n\nYour personalized checklist is just one click away.",
            "next": "q_other_legal_issues"
        },

            "q_other_legal_issues": {
                "type": "question",
                "text": "Do you have any other legal issues that have not been addressed?",
                "yes": "out_final_see_attorney",
                "no": "end_of_quiz" # Finished!
            },
            "out_final_see_attorney": {
                "type": "outcome",
                "level": "Red",
                "text": "You should see a legal assistance attorney to discuss your other legal issues.",
                "next": "end_of_quiz" # Finished!
            },


            # =================================================================
            # END OF QUIZ
            # =================================================================
            "end_of_quiz": {
                "type": "section_intro",
                "title": "Questionnaire Complete",
                "text": "You have completed the Legal Readiness questionnaire. The checklist with your results will be generated now.",
                "next": None
            }
        }
        
        # --- End of self.nodes dictionary ---

        self.current_node_id = "start"
        self.checklist = []

    def get_current_node(self):
        """Returns the current question or outcome node from the dictionary."""
        return self.nodes.get(self.current_node_id)

    def process_answer(self, answer):
        """
        Processes a 'yes' or 'no' answer, moves to the next node,
        and handles any resulting outcomes.
        """
        current_node = self.get_current_node()
        if current_node.get('type') != 'question':
            return

        next_node_id = current_node.get(answer.lower())
        if not next_node_id:
            # This can happen if a question is missing a yes/no path.
            print(f"ERROR: No path for answer '{answer}' from node '{self.current_node_id}'")
            self.current_node_id = "end_of_quiz" # Fail safe
            return

        self.current_node_id = next_node_id
        
        # Automatically process any outcome nodes we land on.
        # This loop allows us to chain outcomes to the next question.
        new_node = self.get_current_node()
        while new_node and new_node.get('type') == 'outcome':
            if new_node.get('level') in ['Red', 'Yellow']:
                # Add the issue to the user's personalized checklist.
                self.checklist.append({
                    "level": new_node['level'],
                    "text": new_node['text']
                })
            
            # Move to the next step defined after the outcome.
            if new_node.get('next'):
                self.current_node_id = new_node['next']
                new_node = self.get_current_node()
            else:
                # If an outcome has no 'next', it's a dead end. Stop the loop.
                break
def get_current_section_title(self):
    """
    Helper function to find the title of the current section by searching backwards
    from the current question to find the last 'section_intro' node.
    """
    # Create a reverse map for easier lookups.
    parent_map = {}
    for key, value in self.nodes.items():
        if 'next' in value:
            parent_map[value['next']] = key
        if 'yes' in value:
            parent_map[value['yes']] = key
        if 'no' in value:
            parent_map[value['no']] = key

    # Trace back from the current node until we find a section intro.
    temp_node_id = self.current_node_id
    for _ in range(len(self.nodes)): # Safety break to prevent infinite loops
        node = self.nodes.get(temp_node_id, {})
        if node.get('type') == 'section_intro' and 'title' in node:
            return node['title']
        
        # Move to the parent node for the next loop
        temp_node_id = parent_map.get(temp_node_id)
        if not temp_node_id:
            return "Section" # Return a default if no title is found
    
    return "Section" # Return a default if no title is found


    def run_quiz_in_terminal(self):
        """
        A simple text-based loop to run the entire quiz for testing purposes
        in a terminal or command prompt.
        """
        while self.current_node_id:
            node = self.get_current_node()
            if not node:
                print(f"FATAL ERROR: Node '{self.current_node_id}' not found. Stopping.")
                break

            node_type = node.get('type')

            if node_type == 'question':
                # Print the question and get user input.
                print(f"\nQ: {node['text']}")
                answer = input("Answer (yes/no): ").lower().strip()
                while answer not in ['yes', 'no']:
                    answer = input("Invalid input. Please enter 'yes' or 'no': ").lower().strip()
                self.process_answer(answer)

            elif node_type == 'section_intro':
                # Display intro text and automatically move to the next node.
                print(f"\n--- {node.get('title', 'Introduction')} ---")
                print(node['text'])
                self.current_node_id = node.get('next')

            else:
                # If we hit the end_of_quiz node or any other node type, stop.
                break

        # --- Post-Quiz Summary ---
        print("\n" + "="*40)
        print("--- Quiz Complete ---")
        print("="*40)
        
        if self.checklist:
            print("\nYour Personalized Legal Readiness Checklist:")
            # Sort the checklist to show Red items first.
            self.checklist.sort(key=lambda item: item['level'], reverse=True)
            for item in self.checklist:
                print(f"- [{item['level'].upper()}] {item['text']}")
        else:
            print("\nCongratulations! No immediate legal actions are recommended based on your answers.")
        
        print("\nDisclaimer: This tool provides general information and is not a substitute for legal advice from a licensed attorney.")


# --- This is the part of the script that makes it runnable ---
# if __name__ == "__main__":
#     quiz_instance = LegalReadinessQuiz()
#     quiz_instance.run_quiz_in_terminal()
