import 'package:flutter/material.dart';

/// Editorial seed; mount as MaterialApp.home and supply host light/dark themes.
class SwissEditorialExample extends StatefulWidget {
  const SwissEditorialExample({super.key});

  @override
  State<SwissEditorialExample> createState() => _SwissEditorialExampleState();
}

class _SwissEditorialExampleState extends State<SwissEditorialExample> {
  final _search = TextEditingController();
  final _saved = <String>{};
  var _category = 'All';
  static const _stories = [
    (id: '01', category: 'Design', title: 'Less noise. More meaning.', summary: 'On making room for the things that deserve our attention.', body: 'Start with what matters. Give the content room to breathe, and let the next action speak for itself.'),
    (id: '02', category: 'Culture', title: 'The city is a type specimen.', summary: 'A field guide to the letters we walk past every day.', body: 'Shopfronts, station signs, and handwritten notices tell a living story about a neighbourhood.'),
    (id: '03', category: 'Design', title: 'A grid is a starting point.', summary: 'Structure that makes space for an unexpected idea.', body: 'Align what belongs together, and break the pattern only when the content gives you a reason.'),
  ];

  @override
  void dispose() {
    _search.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colors = theme.colorScheme;
    final query = _search.text.trim().toLowerCase();
    final visible = _stories.where((story) =>
      (_category == 'All' || story.category == _category) &&
      '${story.title} ${story.summary}'.toLowerCase().contains(query),
    ).toList();
    final buttonStyle = OutlinedButton.styleFrom(
      minimumSize: const Size(48, 48),
      shape: const RoundedRectangleBorder(),
      side: BorderSide(color: colors.onSurface),
    );

    return Scaffold(
      backgroundColor: colors.surface,
      body: SafeArea(
        child: LayoutBuilder(builder: (context, constraints) {
          final compact = constraints.maxWidth < 600;
          return Align(
            alignment: Alignment.topCenter,
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 880),
              child: ListView(
                padding: EdgeInsets.all(compact ? 16 : 32),
                children: [
                  Text('FORM / FIELD', style: theme.textTheme.titleLarge?.copyWith(fontWeight: FontWeight.w800)),
                  const SizedBox(height: 24),
                  const Text('Volume 01 / The clarity issue'),
                  const SizedBox(height: 24),
                  Semantics(header: true, child: Text('A little less. A lot more.', style: theme.textTheme.displaySmall?.copyWith(fontWeight: FontWeight.w800))),
                  const SizedBox(height: 16),
                  const Text('Notes on thoughtful design and everyday life.'),
                  const SizedBox(height: 32),
                  Semantics(header: true, child: Text('The index', style: theme.textTheme.headlineMedium)),
                  const SizedBox(height: 16),
                  TextField(
                    controller: _search,
                    onChanged: (_) => setState(() {}),
                    decoration: const InputDecoration(labelText: 'Search the journal', border: OutlineInputBorder(borderRadius: BorderRadius.zero), constraints: BoxConstraints(minHeight: 48)),
                  ),
                  const SizedBox(height: 16),
                  Wrap(spacing: 8, runSpacing: 8, children: [
                    for (final category in ['All', 'Design', 'Culture'])
                      ConstrainedBox(
                        constraints: const BoxConstraints(minHeight: 48, minWidth: 48),
                        child: FilterChip(
                          label: Text(category),
                          selected: _category == category,
                          showCheckmark: true,
                          materialTapTargetSize: MaterialTapTargetSize.padded,
                          onSelected: (_) => setState(() => _category = category),
                        ),
                      ),
                  ]),
                  const SizedBox(height: 16),
                  Semantics(liveRegion: true, child: Text('${visible.length} ${visible.length == 1 ? 'story' : 'stories'} / ${_saved.length} saved')),
                  for (final story in visible) ...[
                    const SizedBox(height: 24),
                    Divider(color: colors.outline),
                    const SizedBox(height: 16),
                    Text('${story.id} / ${story.category}'),
                    const SizedBox(height: 16),
                    Semantics(header: true, child: Text(story.title, style: theme.textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.w700))),
                    const SizedBox(height: 16),
                    Text(story.summary),
                    const SizedBox(height: 16),
                    Text(story.body),
                    const SizedBox(height: 16),
                    Align(
                      alignment: AlignmentDirectional.centerStart,
                      child: Semantics(
                        selected: _saved.contains(story.id),
                        child: OutlinedButton(
                          style: buttonStyle,
                          onPressed: () => setState(() {
                            if (!_saved.add(story.id)) _saved.remove(story.id);
                          }),
                          child: Text('${_saved.contains(story.id) ? '✓ Saved' : '+ Save'}: ${story.title}'),
                        ),
                      ),
                    ),
                  ],
                  if (visible.isEmpty) ...[
                    const SizedBox(height: 24),
                    const Text('No stories found'),
                    OutlinedButton(
                      style: buttonStyle,
                      onPressed: () => setState(() { _search.clear(); _category = 'All'; }),
                      child: const Text('Reset filters'),
                    ),
                  ],
                  const SizedBox(height: 32),
                  const Text('Fictional journal. Bookmarks stay in this session.'),
                ],
              ),
            ),
          );
        }),
      ),
    );
  }
}

// Verification: analyze and widget tests; hardware accessibility remains a host integration check.
// Fallback: native controls, system typography, no blur/shadow; retain selected state and content order.
