# loans

This started off as just so much more idiarrhea but then became fun to think about (and then after 5 mins of research became a very unoriginal idea, but still!)

It would just be a fun exercise to go through the motions and make a, for example, PawnShop SaaS site that anyone can use to operate a real, physical pawn shop that loans Ether for hocked items of any kind. Situation evolving. 👂

## Original Spewage:

---

`Pawn.sol` -- Provide enough auditing and reigor to allow loans on the Ethereum network to be secured by pawning real-world objects.
The contract is owned by a "reputable address". When you show up and (perhaps physically) relenquish an item in exchange for a loan, registered with a unique loan ID. You can ONLY sign if your address and loan ID match up to a record in the system. Signing triggers an automatic payment to you of `_loanAmount`, meanwhile, you know that those in control of "reputable address" are in possetion of the item securing the loan, recorded as `_inventoryID`

This stuff can for sure get out of control complicated. Maybe this deserves lots of "interface" treatment like you see in [these folks' contracts](https://github.com/gnosis/safe-contracts/tree/186a21a74b327f17fc41217a927dea7064f74604).

* `startPawnAgreement(_inventoryID uint, _loanAmount uint, _pawnee address, _pawnID uint, _payoffAmount uint)` -- When someone shows up to the pawn shop with `_inventoryID` thing and you agree to loan `_loanAmount` to `_pawnee`, requiring the amount of `_payoffAmount` in order for the borrower to recover their item. Note that `_payOffAmount < _loanAmount` need not be forbidden. Maybe this is a parent giving their kid a break with negative interest...? Or maybe this is the European Union and they are doing the same thing.
* `signPawnAgreement(_pawnID)` -- signing is only allowed when `startPawnAgreement` has completed successfully for the given `pawnID`. Calling this triggers an automatic payment of `_loanAmount` to `_pawnee`. This ends the first phase of the transaction ISO compliant pawn brokering. The pawn shop now has your guitar, and when you call this method, you will immediately get your Ether.
* `tweakDealExpiration(???) (???)` -- somehow we need to deal with "expiration" of the deal. If you run out of time, we need to be able to sell your stuff. That's how it works. A nice, neat, logical way to set and maybe adjust the "expiration" is needed. Do we worry much about time stamps here? What exactly keeps a miner from having a grossly-wrong clock? This is a placeholder for such a set of methods (or...)
* `proposeSettlement(_pawnID uint) (_settlementProposalID uint)` -- Borrower is saying "hey, I believe this debt to be satisfied, and am declaring so before the expiration date. You, lender, may now sign indicating agreement, referencing this settlement proposal ID, and return my property, please. Possetion of the 
* `comfirmSettlment(_settlementProposalID) (_inventoryID uint)` -- Um, getting a little bit sloppy. Needs atention. _settlementProposalID should map all the way back to _inventoryID . The point is, we want to record that the property was returned, somehow. Hash of photograph of borrower holding his guitar and today's newspaper?
* `isSettled(_pawnId) (bool)` -- don't know. This needs thinking too.
* ...?
* `showLoawnAgreement(_pawnID uint)` -- I don't know, say you've lost your paperwork. All of the critical info is on the contract, why not have (require) a method to display it? Maybe this could be a `MAY`, in RFC-speak.
* How do we "compose" this with advanced features?
   1. Tour the world of money-borrowing and understand what all the distinct pieces are (orthagonal interfaces)
   1. Maybe, I mean, you could actually strike up a conversation on r/Pawn (or whatever). Why not?
* If you're going to pawn something digital, it's more likely to be an NFT than an ERC20. Or, maybe fungilbe is on a continum. You might have an ERC20 that you can prove is the first-ever minted FooCoin (maybe even that fact will never really earn a premium). Also (!!) you and your trading partner might have opposite opinions about the coins loaned (you think they are one the way down, tradee thinks on the way up) and the collatoral used (same). So I see it is accepting attractive, fine cloth as collateral in exchange for lending ragged, clipped denariuses. Meanwhile the borrower sees it as giving his dishrags as collateral in exchanged for some robust Romain coinage. Both parties "benefit". Even though it seems like for like.
* deadline*S* for payment*S*: we might want that.
