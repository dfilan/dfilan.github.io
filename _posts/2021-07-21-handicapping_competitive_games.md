---
layout: post
title: "Handicapping competitive games"
date: 2021-07-21
---

[epistemic status: thing I thought of while falling asleep and just wrote up]

Suppose you're playing a competitive game. By that, I mean a game where there are multiple players, and each is trying to win by beating the others. An example of a game like this is Go. But, if you think about it, soccer is also kind of like this: each 'player' is composed of a team of people, and the two 'players' are competing against each other. We'll say that that also counts.

Sometimes, you'd like to play a competitive game with a friend or multiple friends, but the problem is that one of you is stronger than the other. It's easy to see what this means in Go, and in the case of soccer, you could imagine that you're part of a pre-set team, and so are your friends, and it wouldn't be as fun to swap people between teams to even it out (perhaps because e.g. the teams are based on where you live). This is kind of sad because it means that by default, the stronger player or team will predictably win, which makes it a bit less fun. A way to get around this is by handicapping the stronger player: giving them some disadvantage so that the weaker player has a decent chance of winning, even if the stronger player tries their best. In Go, the standard way of doing this is to have the weaker player start with some well-placed stones already on the board. I don't know how exactly this works in soccer - perhaps by having the stronger team play with fewer members than usual?

If you're in this situation, but you don't know the standard way to handicap - for instance, if you're me and the game is soccer - it might be useful to have a taxonomy of ways to handicap games to choose between. Or if you're bored of the standard way of handicapping, a taxonomy might inspire you to create new ideas. In this post, I'll detail what I think is an exhaustive taxonomy.

To think about how to handicap competitive games, I find it helpful to think about what a competitive game is. I think that a competitive game is specified by the following things:
- A starting state
- A number of players in the game
- A set of options for what the players can do at any point
- A win condition
- A 'transition function', which determines how the game state changes after each player does something
- An 'observability function', which determines what each player can see about the game state
These all provide candidates to tweak. Let's go thru them one by one.

One way of handicapping is to change the starting state in order to give one player an initial advantage. This is how I'd think about handicapping in Go: the weaker player starts with more stones on the board than the stronger player [1]. In soccer, you could imagine the kick-off happening closer to the stronger team's goal, which might make it easier for the weaker player to score. I'd say this is usually a good option.

I don't think it really makes sense to vary the number of players in the game - in soccer and Go this wouldn't make much sense, and in general it's hard to see how this would help the weaker player relative to the stronger player.

Changing the set of options for the players can be a possible handicapping scheme. In Go, it's hard to see how to do this without significantly changing the game - the closest thing I can think of is banning the stronger player from playing on certain points on the board, or maybe forbidding the stronger player from killing or cutting groups. I think it makes more sense in soccer, however: one team could accept a limitation on how fast they can run. In order not to change the game, I imagine it will usually look like narrowing the option set for the stronger player, since enlarging the option set for the weaker player seems like it would significantly change the game.

The win condition can be a promising way to handicap, especially for points-based games like Go and soccer: one can simply add some number of points to the weaker player's total at the end, before deciding the winner [2]. Especially in Go, I think this handicap system is under-used - in my opinion, it changes the game less than giving the weaker player handicap stones on the board at the start. However, it's less clear how to apply it in games that do not determine the winner by keeping a score, such as chess.

The transition function is pretty core to the identity of a game, and therefore not to be trifled with. That being said, it's possible that minor tweaks could provide a decent handicapping system - for instance, one could imagine a high-tech soccer ball that acted as tho it was heavier when the stronger team kicked it and lighter when the weaker team kicked it, or a version of Go where 5% of the time the stronger player's move was replaced by a random move.

The observability function seems easier to tweak while retaining the character of a game. In Go, for example, one player could be required to play without seeing the board, only hearing the coordinates of each move and saying the coordinates they would like to play on. A less extreme case would be to use technology to allow the weaker player to see which stones are which colour, but make the stones' identities invisible to the stronger player. In order to adjust the degree of handicap, one could change the number of moves in which this observability constraint applies. For soccer, you could imagine requiring one team to wear glasses that slightly distorted their vision.

That concludes my list of aspects of a game to tweak for handicapping. But there's one more crucial ingredient that goes into playing a game - the computation available to each player. One can handicap a player by limiting the computation they have available. For instance, in Go, one could use asymmetric time controls, where the weaker player gets more time to think about their moves than the stronger player. In soccer, this could look like requiring all members of the stronger team to use earplugs, so that they can't communicate with one another as easily [3].

I think this is an exhaustive taxonomy. I also think it's useful: as far as I'm aware, most ways of handicapping fall pretty cleanly into just one of these, and it's helped me come up with handicap ideas (in the process of writing the post). I hope you also find it useful.

[1] If the weaker player gets to choose where to put the stones, then this isn't quite just a modification of the starting state. But normally the stones are put in a set position.

[2] This could also be seen as a modification of the starting state.

[3] This also changes the observability function, but I think that's not its main effect.
