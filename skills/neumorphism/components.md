# Neumorphism — Component Anatomy & Recipes

## Loading state
For asynchronous actions, preserve the control footprint and expose busy state semantically. Keep the label stable when practical, disable duplicate activation while busy, and use a progress indicator or text cue in addition to any pressed/inset decoration. Loading must not be communicated through shadow changes alone.
