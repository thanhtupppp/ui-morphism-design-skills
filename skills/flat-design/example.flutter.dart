import 'package:flutter/material.dart';

/// Flat Design reference implementation.
///
/// The example intentionally relies on native Flutter semantics and keeps
/// hierarchy in color, type, spacing, borders, and explicit states rather
/// than decorative depth.
class FlatDesignExample extends StatelessWidget {
  const FlatDesignExample({super.key});

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    final text = Theme.of(context).textTheme;

    return Scaffold(
      backgroundColor: scheme.surface,
      appBar: AppBar(
        elevation: 0,
        title: const Text('Operations'),
        actions: [
          IconButton(
            tooltip: 'Notifications',
            onPressed: () {},
            icon: const Icon(Icons.notifications_outlined),
          ),
        ],
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          final compact = constraints.maxWidth < 600;
          return ListView(
            padding: EdgeInsets.all(compact ? 16 : 24),
            children: [
              Text('Operations overview', style: text.headlineSmall),
              const SizedBox(height: 8),
              Text(
                'Clear hierarchy comes from type, spacing, grouping, and explicit states.',
                style: text.bodyMedium,
              ),
              const SizedBox(height: 16),
              const _FlatAlert(),
              const SizedBox(height: 16),
              _FlatForm(compact: compact),
              const SizedBox(height: 24),
              _FlatStatusCard(scheme: scheme),
              const SizedBox(height: 24),
              _FlatTable(compact: compact),
              const SizedBox(height: 24),
              _FlatTabs(),
            ],
          );
        },
      ),
    );
  }
}

class _FlatAlert extends StatelessWidget {
  const _FlatAlert();

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: scheme.errorContainer,
        border: Border.all(color: scheme.error),
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(Icons.error_outline, color: scheme.onErrorContainer),
          const SizedBox(width: 12),
          Expanded(
            child: Text(
              'One device requires attention. Check the maintenance queue.',
              style: TextStyle(color: scheme.onErrorContainer),
            ),
          ),
        ],
      ),
    );
  }
}

class _FlatForm extends StatelessWidget {
  const _FlatForm({required this.compact});
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final fields = [
      const TextField(
        decoration: InputDecoration(
          labelText: 'Search equipment',
          border: OutlineInputBorder(),
        ),
      ),
      DropdownButtonFormField<String>(
        decoration: const InputDecoration(
          labelText: 'Status',
          border: OutlineInputBorder(),
        ),
        items: const [
          DropdownMenuItem(value: 'all', child: Text('All statuses')),
          DropdownMenuItem(value: 'active', child: Text('Active')),
          DropdownMenuItem(value: 'attention', child: Text('Needs attention')),
        ],
        onChanged: (_) {},
      ),
    ];

    final content = compact
        ? Column(children: [fields[0], const SizedBox(height: 12), fields[1]])
        : Row(children: [Expanded(child: fields[0]), const SizedBox(width: 12), Expanded(child: fields[1])]);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('Filters', style: Theme.of(context).textTheme.titleMedium),
        const SizedBox(height: 12),
        content,
        const SizedBox(height: 12),
        Row(
          children: [
            FilledButton.icon(
              onPressed: () {},
              icon: const Icon(Icons.search),
              label: const Text('Apply filters'),
            ),
            const SizedBox(width: 8),
            OutlinedButton(onPressed: () {}, child: const Text('Reset')),
          ],
        ),
      ],
    );
  }
}

class _FlatStatusCard extends StatelessWidget {
  const _FlatStatusCard({required this.scheme});
  final ColorScheme scheme;

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 0,
      margin: EdgeInsets.zero,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8),
        side: BorderSide(color: scheme.outline),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          children: [
            Expanded(child: Text('System availability', style: Theme.of(context).textTheme.titleMedium)),
            const SizedBox(width: 12),
            Chip(
              avatar: Icon(Icons.check_circle, size: 18, color: scheme.primary),
              label: const Text('Healthy'),
            ),
          ],
        ),
      ),
    );
  }
}

class _FlatTable extends StatelessWidget {
  const _FlatTable({required this.compact});
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final rows = [
      const ('AHU-01', 'Active', '72%'),
      const ('AHU-02', 'Attention', '41%'),
      const ('AHU-03', 'Active', '88%'),
    ];

    final table = DataTable(
      columns: const [
        DataColumn(label: Text('Equipment')),
        DataColumn(label: Text('Status')),
        DataColumn(label: Text('Load')),
      ],
      rows: rows
          .map(
            (row) => DataRow(cells: [
              DataCell(Text(row.$1)),
              DataCell(Text(row.$2)),
              DataCell(Text(row.$3)),
            ]),
          )
          .toList(),
    );

    return compact
        ? SingleChildScrollView(scrollDirection: Axis.horizontal, child: table)
        : table;
  }
}

class _FlatTabs extends StatelessWidget {
  const _FlatTabs();

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const TabBar(tabs: [
            Tab(text: 'Overview'),
            Tab(text: 'History'),
            Tab(text: 'Alerts'),
          ]),
          const SizedBox(height: 16),
          SizedBox(
            height: 48,
            child: TabBarView(children: [
              const Text('Current operational summary.'),
              const Text('Historical readings and events.'),
              const Text('Open and resolved alerts.'),
            ]),
          ),
        ],
      ),
    );
  }
}
