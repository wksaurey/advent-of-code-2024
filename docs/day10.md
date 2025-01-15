create a trailhead object for every trailhead 
add all trailhead objects to trailheads list
create a trail object for every trailhead object (including link to trailheads list)
add each trail to the trails linked list

pop the first trail from trails
check u d l r from last section location of trail
    if greater than the section value by 1
        create trail copy with new section appended
        if new section value is 9
            add trail copy to complete trails
            increase linked trailhead object score by 1
        else
            add to end of linked list

when trails linked list is empty
    sum the trailheads scores