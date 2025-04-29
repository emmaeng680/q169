from django.core.management.base import BaseCommand
from tracker.models import QuestionCollection, Topic, Question

class Command(BaseCommand):
    help = 'Import Grind169 questions'

    def handle(self, *args, **kwargs):
        # Create or get the Grind169 collection
        grind169, created = QuestionCollection.objects.get_or_create(
            name='Grind169',
            defaults={'description': 'A curated list of 169 leetcode questions to help you ace the coding interviews.'}
        )
        
        # Import Array topic questions
        self.import_array_questions(grind169)
        
        # Import Graph topic questions
        self.import_graph_questions(grind169)

        # Import Binary Tree topic questions
        self.import_binary_tree_questions(grind169)

        # Import Stack topic questions
        self.import_stack_questions(grind169)

        # Import Linked List topic questions
        self.import_linked_list_questions(grind169)

        # Import String topic questions
        self.import_string_questions(grind169)

        # Import Dynamic Programming topic questions
        self.import_dynamic_programming_questions(grind169)

        # Import Heap topic questions
        self.import_heap_questions(grind169)

        # Import Binary Search topic questions
        self.import_binary_search_questions(grind169)

        # Import Binary topic questions
        self.import_binary_questions(grind169)

        # Import Recursion topic questions
        self.import_recursion_questions(grind169)

        # Import Math topic questions
        self.import_math_questions(grind169)

        # Import Matrix topic questions
        self.import_matrix_questions(grind169)

        # Import Binary Search Tree topic questions
        self.import_binary_search_tree_questions(grind169)

        # Import Trie topic questions
        self.import_trie_questions(grind169)

        # Import Hash Table topic questions
        self.import_hash_table_questions(grind169)

        # Import Design topic questions
        self.import_design_questions(grind169)





    
    def import_array_questions(self, grind169):
        # Sample data provided by the user - Array topic questions
        array_topic, _ = Topic.objects.get_or_create(
            name='Array',
            collection=grind169
        )
        
        # Add array questions
        array_questions = [
            ('Two Sum', 'https://leetcode.com/problems/two-sum/description/'),
            ('Best Time to Buy and Sell Stock', 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/'),
            ('Insert Interval', 'https://leetcode.com/problems/insert-interval/description/'),
            ('3Sum', 'https://leetcode.com/problems/3sum/description/'),
            ('Product of Array Except Self', 'https://leetcode.com/problems/product-of-array-except-self/description/'),
            ('Combination Sum', 'https://leetcode.com/problems/combination-sum/description/'),
            ('Merge Intervals', 'https://leetcode.com/problems/merge-intervals/description/'),
            ('Majority Element', 'https://leetcode.com/problems/majority-element/description/'),
            ('Sort Colors', 'https://leetcode.com/problems/sort-colors/description/'),
            ('Contains Duplicate', 'https://leetcode.com/problems/contains-duplicate/description/'),
            ('Container With Most Water', 'https://leetcode.com/problems/container-with-most-water/description/'),
            ('Meeting Rooms', 'https://www.geeksforgeeks.org/problems/attend-all-meetings/0'),
            ('Gas Station', 'https://leetcode.com/problems/gas-station/description/'),
            ('Longest Consecutive Sequence', 'https://leetcode.com/problems/longest-consecutive-sequence/description/'),
            ('Rotate Array', 'https://leetcode.com/problems/rotate-array/description/'),
            ('Contiguous Array', 'https://leetcode.com/problems/contiguous-array/description/'),
            ('Subarray Sum Equals K', 'https://leetcode.com/problems/subarray-sum-equals-k/description/'),
            ('Employee Free Time', 'https://www.naukri.com/code360/problems/employee-free-time_1171181'),
            ('Move Zeroes', 'https://leetcode.com/problems/move-zeroes/description/'),
            ('Meeting Rooms II', 'https://www.geeksforgeeks.org/problems/attend-all-meetings-ii/1'),
            ('Sliding Window Maximum', 'https://leetcode.com/problems/sliding-window-maximum/description/'),
            ('Squares of a Sorted Array', 'https://leetcode.com/problems/squares-of-a-sorted-array/description/'),
            ('3Sum Closest', 'https://leetcode.com/problems/3sum-closest/description/'),
            ('Non-overlapping Intervals', 'https://leetcode.com/problems/non-overlapping-intervals/description/'),
        ]
        
        count = 0
        for title, link in array_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=array_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} array questions for Grind169'))
    
    def import_graph_questions(self, grind169):
        # Create Graph topic
        graph_topic, _ = Topic.objects.get_or_create(
            name='Graph',
            collection=grind169
        )
        
        # Add graph questions
        graph_questions = [
            ('Flood Fill', 'https://leetcode.com/problems/flood-fill/description/'),
            ('01 Matrix', 'https://leetcode.com/problems/01-matrix/description/'),
            ('Clone Graph', 'https://leetcode.com/problems/clone-graph/description/'),
            ('Course Schedule', 'https://leetcode.com/problems/course-schedule/description/'),
            ('Number of Islands', 'https://leetcode.com/problems/number-of-islands/description/'),
            ('Rotting Oranges', 'https://leetcode.com/problems/rotting-oranges/description/'),
            ('Accounts Merge', 'https://leetcode.com/problems/accounts-merge/description/'),
            ('Word Ladder', 'https://leetcode.com/problems/word-ladder/description/'),
            ('Word Search', 'https://leetcode.com/problems/word-search/description/'),
            ('Minimum Height Trees', 'https://leetcode.com/problems/minimum-height-trees/description/'),
            ('Pacific Atlantic Water Flow', 'https://leetcode.com/problems/pacific-atlantic-water-flow/description/'),
            ('Shortest Path to Get Food', 'https://www.naukri.com/code360/problems/shortest-path_920528'),
            ('Graph Valid Tree', 'https://www.geeksforgeeks.org/problems/is-it-a-tree/0'),
            ('Course Schedule II', 'https://leetcode.com/problems/course-schedule-ii/description/'),
            ('Number of Connected Components in an Undirected Graph', 'https://www.geeksforgeeks.org/problems/connected-components-in-an-undirected-graph/1'),
            ('Minimum Knight Moves', 'https://www.geeksforgeeks.org/problems/steps-by-knight5927/1'),
            ('Longest Increasing Path in a Matrix', 'https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/'),
            ('Word Search II', 'https://leetcode.com/problems/word-search-ii/description/'),
            ('Alien Dictionary', 'https://www.geeksforgeeks.org/problems/alien-dictionary/1'),
            ('Bus Routes', 'https://leetcode.com/problems/bus-routes/description/'),
            ('Cheapest Flights Within K Stops', 'https://leetcode.com/problems/cheapest-flights-within-k-stops/description/'),
        ]
        
        count = 0
        for title, link in graph_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=graph_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} graph questions for Grind169'))


    def import_binary_tree_questions(self, grind169):
        # Create Binary Tree topic
        binary_tree_topic, _ = Topic.objects.get_or_create(
            name='Binary Tree',
            collection=grind169
        )
        
        # Add binary tree questions
        binary_tree_questions = [
            ('Invert Binary Tree', 'https://leetcode.com/problems/invert-binary-tree/description/'),
            ('Balanced Binary Tree', 'https://leetcode.com/problems/balanced-binary-tree/description/'),
            ('Binary Tree Level Order Traversal', 'https://leetcode.com/problems/binary-tree-level-order-traversal/description/'),
            ('Lowest Common Ancestor of a Binary Tree', 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/'),
            ('Serialize and Deserialize Binary Tree', 'https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/'),
            ('Diameter of Binary Tree', 'https://leetcode.com/problems/diameter-of-binary-tree/description/'),
            ('Binary Tree Right Side View', 'https://leetcode.com/problems/binary-tree-right-side-view/description/'),
            ('Maximum Depth of Binary Tree', 'https://leetcode.com/problems/maximum-depth-of-binary-tree/description/'),
            ('Construct Binary Tree from Preorder and Inorder Traversal', 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/'),
            ('Binary Tree Maximum Path Sum', 'https://leetcode.com/problems/binary-tree-maximum-path-sum/description/'),
            ('Path Sum II', 'https://leetcode.com/problems/path-sum-ii/description/'),
            ('Maximum Width of Binary Tree', 'https://leetcode.com/problems/maximum-width-of-binary-tree/description/'),
            ('Same Tree', 'https://leetcode.com/problems/same-tree/description/'),
            ('Binary Tree Zigzag Level Order Traversal', 'https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/'),
            ('Path Sum III', 'https://leetcode.com/problems/path-sum-iii/description/'),
            ('Symmetric Tree', 'https://leetcode.com/problems/symmetric-tree/description/'),
            ('All Nodes Distance K in Binary Tree', 'https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/'),
            ('Subtree of Another Tree', 'https://leetcode.com/problems/subtree-of-another-tree/description/'),
        ]
        
        count = 0
        for title, link in binary_tree_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=binary_tree_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} binary tree questions for Grind169'))


    def import_stack_questions(self, grind169):
        # Create Stack topic
        stack_topic, _ = Topic.objects.get_or_create(
            name='Stack',
            collection=grind169
        )
        
        # Add stack questions
        stack_questions = [
            ('Valid Parentheses', 'https://leetcode.com/problems/valid-parentheses/description/'),
            ('Implement Queue using Stacks', 'https://leetcode.com/problems/implement-queue-using-stacks/description/'),
            ('Evaluate Reverse Polish Notation', 'https://leetcode.com/problems/evaluate-reverse-polish-notation/description/'),
            ('Min Stack', 'https://leetcode.com/problems/min-stack/description/'),
            ('Trapping Rain Water', 'https://leetcode.com/problems/trapping-rain-water/description/'),
            ('Basic Calculator', 'https://leetcode.com/problems/basic-calculator/description/'),
            ('Largest Rectangle in Histogram', 'https://leetcode.com/problems/largest-rectangle-in-histogram/description/'),
            ('Daily Temperatures', 'https://leetcode.com/problems/daily-temperatures/description/'),
            ('Backspace String Compare', 'https://leetcode.com/problems/backspace-string-compare/description/'),
            ('Maximum Frequency Stack', 'https://leetcode.com/problems/maximum-frequency-stack/description/'),
            ('Decode String', 'https://leetcode.com/problems/decode-string/description/'),
            ('Asteroid Collision', 'https://leetcode.com/problems/asteroid-collision/description/'),
            ('Longest Valid Parentheses', 'https://leetcode.com/problems/longest-valid-parentheses/description/'),
            ('Basic Calculator II', 'https://leetcode.com/problems/basic-calculator-ii/description/'),
        ]
        
        count = 0
        for title, link in stack_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=stack_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} stack questions for Grind169'))

    def import_linked_list_questions(self, grind169):
        # Create Linked List topic
        linked_list_topic, _ = Topic.objects.get_or_create(
            name='Linked List',
            collection=grind169
        )
        
        # Add linked list questions
        linked_list_questions = [
            ('Merge Two Sorted Lists', 'https://leetcode.com/problems/merge-two-sorted-lists/description/'),
            ('Linked List Cycle', 'https://leetcode.com/problems/linked-list-cycle/description/'),
            ('Reverse Linked List', 'https://leetcode.com/problems/reverse-linked-list/description/'),
            ('Middle of the Linked List', 'https://leetcode.com/problems/middle-of-the-linked-list/description/'),
            ('LRU Cache', 'https://leetcode.com/problems/lru-cache/description/'),
            ('Remove Nth Node From End of List', 'https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/'),
            ('Swap Nodes in Pairs', 'https://leetcode.com/problems/swap-nodes-in-pairs/description/'),
            ('Odd Even Linked List', 'https://leetcode.com/problems/odd-even-linked-list/description/'),
            ('Add Two Numbers', 'https://leetcode.com/problems/add-two-numbers/description/'),
            ('Sort List', 'https://leetcode.com/problems/sort-list/description/'),
            ('Palindrome Linked List', 'https://leetcode.com/problems/palindrome-linked-list/description/'),
            ('Reorder List', 'https://leetcode.com/problems/reorder-list/description/'),
            ('Rotate List', 'https://leetcode.com/problems/rotate-list/description/'),
            ('Reverse Nodes in k-Group', 'https://leetcode.com/problems/reverse-nodes-in-k-group/description/'),
        ]
        
        count = 0
        for title, link in linked_list_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=linked_list_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} linked list questions for Grind169'))

    def import_string_questions(self, grind169):
        # Create String topic
        string_topic, _ = Topic.objects.get_or_create(
            name='String',
            collection=grind169
        )
        
        # Add string questions
        string_questions = [
            ('Valid Palindrome', 'https://leetcode.com/problems/valid-palindrome/description/'),
            ('Valid Anagram', 'https://leetcode.com/problems/valid-anagram/description/'),
            ('Longest Substring Without Repeating Characters', 'https://leetcode.com/problems/longest-substring-without-repeating-characters/description/'),
            ('Longest Palindrome', 'https://leetcode.com/problems/longest-palindrome/description/'),
            ('Minimum Window Substring', 'https://leetcode.com/problems/minimum-window-substring/description/'),
            ('String to Integer (atoi)', 'https://leetcode.com/problems/string-to-integer-atoi/description/'),
            ('Longest Palindromic Substring', 'https://leetcode.com/problems/longest-palindromic-substring/description/'),
            ('Find All Anagrams in a String', 'https://leetcode.com/problems/find-all-anagrams-in-a-string/description/'),
            ('Group Anagrams', 'https://leetcode.com/problems/group-anagrams/description/'),
            ('Longest Repeating Character Replacement', 'https://leetcode.com/problems/longest-repeating-character-replacement/description/'),
            ('Longest Common Prefix', 'https://leetcode.com/problems/longest-common-prefix/description/'),
            ('Largest Number', 'https://leetcode.com/problems/largest-number/description/'),
            ('Encode and Decode Strings', 'https://www.geeksforgeeks.org/problems/encode-and-decode-strings/1'),
            ('Palindrome Pairs', 'https://leetcode.com/problems/palindrome-pairs/description/'),
        ]
        
        count = 0
        for title, link in string_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=string_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} string questions for Grind169'))

    def import_dynamic_programming_questions(self, grind169):
        # Create Dynamic Programming topic
        dynamic_programming_topic, _ = Topic.objects.get_or_create(
            name='Dynamic Programming',
            collection=grind169
        )
        
        # Add dynamic programming questions
        dynamic_programming_questions = [
            ('Maximum Subarray', 'https://leetcode.com/problems/maximum-subarray/description/'),
            ('Coin Change', 'https://leetcode.com/problems/coin-change/description/'),
            ('Climbing Stairs', 'https://leetcode.com/problems/climbing-stairs/description/'),
            ('Partition Equal Subset Sum', 'https://leetcode.com/problems/partition-equal-subset-sum/description/'),
            ('Unique Paths', 'https://leetcode.com/problems/unique-paths/description/'),
            ('House Robber', 'https://leetcode.com/problems/house-robber/description/'),
            ('Maximum Product Subarray', 'https://leetcode.com/problems/maximum-product-subarray/description/'),
            ('Longest Increasing Subsequence', 'https://leetcode.com/problems/longest-increasing-subsequence/description/'),
            ('Jump Game', 'https://leetcode.com/problems/jump-game/description/'),
            ('Maximal Square', 'https://leetcode.com/problems/maximal-square/description/'),
            ('Decode Ways', 'https://leetcode.com/problems/decode-ways/description/'),
            ('Combination Sum IV', 'https://leetcode.com/problems/combination-sum-iv/description/'),
        ]
        
        count = 0
        for title, link in dynamic_programming_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=dynamic_programming_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} dynamic programming questions for Grind169'))

    def import_heap_questions(self, grind169):
        # Create Heap topic
        heap_topic, _ = Topic.objects.get_or_create(
            name='Heap',
            collection=grind169
        )
        
        # Add heap questions
        heap_questions = [
            ('K Closest Points to Origin', 'https://leetcode.com/problems/k-closest-points-to-origin/description/'),
            ('Find Median from Data Stream', 'https://leetcode.com/problems/find-median-from-data-stream/description/'),
            ('Merge k Sorted Lists', 'https://leetcode.com/problems/merge-k-sorted-lists/description/'),
            ('Task Scheduler', 'https://leetcode.com/problems/task-scheduler/description/'),
            ('Top K Frequent Words', 'https://leetcode.com/problems/top-k-frequent-words/description/'),
            ('Find K Closest Elements', 'https://leetcode.com/problems/find-k-closest-elements/description/'),
            ('Kth Largest Element in an Array', 'https://leetcode.com/problems/kth-largest-element-in-an-array/description/'),
            ('Smallest Range Covering Elements from K Lists', 'https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/'),
        ]
        
        count = 0
        for title, link in heap_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=heap_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} heap questions for Grind169'))

    def import_binary_search_questions(self, grind169):
        # Create Binary Search topic
        binary_search_topic, _ = Topic.objects.get_or_create(
            name='Binary Search',
            collection=grind169
        )
        
        # Add binary search questions
        binary_search_questions = [
            ('Binary Search', 'https://leetcode.com/problems/binary-search/description/'),
            ('First Bad Version', 'https://leetcode.com/problems/first-bad-version/description/'),
            ('Search in Rotated Sorted Array', 'https://leetcode.com/problems/search-in-rotated-sorted-array/description/'),
            ('Time Based Key-Value Store', 'https://leetcode.com/problems/time-based-key-value-store/description/'),
            ('Maximum Profit in Job Scheduling', 'https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/'),
            ('Median of Two Sorted Arrays', 'https://leetcode.com/problems/median-of-two-sorted-arrays/description/'),
            ('Search a 2D Matrix', 'https://leetcode.com/problems/search-a-2d-matrix/description/'),
            ('Find Minimum in Rotated Sorted Array', 'https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/'),
        ]
        
        count = 0
        for title, link in binary_search_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=binary_search_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} binary search questions for Grind169'))

    def import_binary_questions(self, grind169):
        # Create Binary topic
        binary_topic, _ = Topic.objects.get_or_create(
            name='Binary',
            collection=grind169
        )
        
        # Add binary questions
        binary_questions = [
            ('Add Binary', 'https://leetcode.com/problems/add-binary/description/'),
            ('Find the Duplicate Number', 'https://leetcode.com/problems/find-the-duplicate-number/description/'),
            ('Counting Bits', 'https://leetcode.com/problems/counting-bits/description/'),
            ('Number of 1 Bits', 'https://leetcode.com/problems/number-of-1-bits/description/'),
            ('Single Number', 'https://leetcode.com/problems/single-number/description/'),
            ('Missing Number', 'https://leetcode.com/problems/missing-number/description/'),
            ('Reverse Bits', 'https://leetcode.com/problems/reverse-bits/description/'),
        ]
        
        count = 0
        for title, link in binary_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=binary_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} binary questions for Grind169'))

    def import_recursion_questions(self, grind169):
        # Create Recursion topic
        recursion_topic, _ = Topic.objects.get_or_create(
            name='Recursion',
            collection=grind169
        )
        
        # Add recursion questions
        recursion_questions = [
            ('Permutations', 'https://leetcode.com/problems/permutations/description/'),
            ('Subsets', 'https://leetcode.com/problems/subsets/description/'),
            ('Letter Combinations of a Phone Number', 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/'),
            ('Next Permutation', 'https://leetcode.com/problems/next-permutation/description/'),
            ('Generate Parentheses', 'https://leetcode.com/problems/generate-parentheses/description/'),
            ('N-Queens', 'https://leetcode.com/problems/n-queens/description/'),
        ]
        
        count = 0
        for title, link in recursion_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=recursion_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} recursion questions for Grind169'))


    def import_math_questions(self, grind169):
        # Create Math topic
        math_topic, _ = Topic.objects.get_or_create(
            name='Math',
            collection=grind169
        )
        
        # Add math questions
        math_questions = [
            ('Roman to Integer', 'https://leetcode.com/problems/roman-to-integer/description/'),
            ('Random Pick with Weight', 'https://leetcode.com/problems/random-pick-with-weight/description/'),
            ('Pow(x, n)', 'https://leetcode.com/problems/powx-n/description/'),
            ('Reverse Integer', 'https://leetcode.com/problems/reverse-integer/description/'),
            ('Palindrome Number', 'https://leetcode.com/problems/palindrome-number/description/'),
        ]
        
        count = 0
        for title, link in math_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=math_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} math questions for Grind169'))


    def import_matrix_questions(self, grind169):
        # Create Matrix topic
        matrix_topic, _ = Topic.objects.get_or_create(
            name='Matrix',
            collection=grind169
        )
        
        # Add matrix questions
        matrix_questions = [
            ('Spiral Matrix', 'https://leetcode.com/problems/spiral-matrix/description/'),
            ('Valid Sudoku', 'https://leetcode.com/problems/valid-sudoku/description/'),
            ('Rotate Image', 'https://leetcode.com/problems/rotate-image/description/'),
            ('Set Matrix Zeroes', 'https://leetcode.com/problems/set-matrix-zeroes/description/'),
            ('Sudoku Solver', 'https://leetcode.com/problems/sudoku-solver/description/'),
        ]
        
        count = 0
        for title, link in matrix_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=matrix_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} matrix questions for Grind169'))

    def import_binary_search_tree_questions(self, grind169):
        # Create Binary Search Tree topic
        binary_search_tree_topic, _ = Topic.objects.get_or_create(
            name='Binary Search Tree',
            collection=grind169
        )
        
        # Add binary search tree questions
        binary_search_tree_questions = [
            ('Lowest Common Ancestor of a Binary Search Tree', 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/'),
            ('Validate Binary Search Tree', 'https://leetcode.com/problems/validate-binary-search-tree/description/'),
            ('Kth Smallest Element in a BST', 'https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/'),
            ('Inorder Successor in BST', 'https://www.geeksforgeeks.org/problems/inorder-successor-in-bst/0'),
            ('Convert Sorted Array to Binary Search Tree', 'https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/'),
        ]
        
        count = 0
        for title, link in binary_search_tree_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=binary_search_tree_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} binary search tree questions for Grind169'))


    def import_trie_questions(self, grind169):
        # Create Trie topic
        trie_topic, _ = Topic.objects.get_or_create(
            name='Trie',
            collection=grind169
        )
        
        # Add trie questions
        trie_questions = [
            ('Implement Trie (Prefix Tree)', 'https://leetcode.com/problems/implement-trie-prefix-tree/description/'),
            ('Word Break', 'https://leetcode.com/problems/word-break/description/'),
            ('Design Add and Search Words Data Structure', 'https://leetcode.com/problems/design-add-and-search-words-data-structure/description/'),
            ('Design In-Memory File System', 'https://www.lintcode.com/problem/3677/'),
        ]
        
        count = 0
        for title, link in trie_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=trie_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} trie questions for Grind169'))

    def import_hash_table_questions(self, grind169):
        # Create Hash Table topic
        hash_table_topic, _ = Topic.objects.get_or_create(
            name='Hash Table',
            collection=grind169
        )
        
        # Add hash table questions
        hash_table_questions = [
            ('Ransom Note', 'https://leetcode.com/problems/ransom-note/'),
            ('Insert Delete GetRandom O(1)', 'https://leetcode.com/problems/insert-delete-getrandom-o1/description/'),
            ('First Missing Positive', 'https://leetcode.com/problems/first-missing-positive/description/'),
        ]
        
        count = 0
        for title, link in hash_table_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=hash_table_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} hash table questions for Grind169'))


    def import_design_questions(self, grind169):
        # Create Design topic
        design_topic, _ = Topic.objects.get_or_create(
            name='Design',
            collection=grind169
        )
        
        # Add design questions
        design_questions = [
            ('Design Hit Counter', 'https://www.naukri.com/code360/problems/hit-counter_1230785'),
            # Add any other design questions you might have here
        ]
        
        count = 0
        for title, link in design_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=grind169,
                topic=design_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} design questions for Grind169'))